from nltk.sentiment import SentimentIntensityAnalyzer
from matplotlib import pyplot as plt
from datetime import datetime
from time import sleep
from typing import Union
from io import StringIO
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import operator
import time
import re

import nltk
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def parse(string_data):
    author_pattern = "<v (.*?)>"
    sentences_pattern = ">(.*?)</v>"
    duration_pattern = "[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]"

    author = re.findall(author_pattern, string_data)
    sentences = re.findall(sentences_pattern, string_data)
    duration = re.findall(duration_pattern, string_data)

    start_times = duration[::2]
    end_times = duration[1::2]

    time_spoken = []

    for end, start in zip(end_times, start_times):
        time = datetime.strptime(end, "%H:%M:%S.%f") - datetime.strptime(
            start, "%H:%M:%S.%f"
        )  # append each difference to list
        time_spoken.append(time.total_seconds())

    df = pd.DataFrame(author, columns=["Names"])
    df["Content"] = sentences
    df["Words"] = df["Content"].apply(lambda x: len(x.split()))
    df["Start"] = start_times
    df["End"] = end_times
    df["Time Spoken (seconds)"] = time_spoken

    df["Total Sentiment"] = df["Content"].apply(
        lambda x: sia.polarity_scores(x)["compound"]
    )
    df["Sentiment Direction"] = np.select(
        [
            df["Total Sentiment"] < 0,
            df["Total Sentiment"] == 0,
            df["Total Sentiment"] > 0,
        ],
        ["Negative", "Neutral", "Positive"],
    )

    with st.expander("Click for table."):
        st.dataframe(df)

    result = (
        df.groupby("Names")["Words", "Time Spoken (seconds)", "Total Sentiment"]
        .sum()
        .reset_index()
    )
    result["WPM"] = round(result["Words"] / (result["Time Spoken (seconds)"] / 60), 1)
    totaltimes = (
        df.groupby("Names").size().reset_index().rename(columns={0: "Times Spoken"})
    )
    final = pd.merge(result, totaltimes, on="Names", how="left")
    final["Sentiment Value"] = final["Total Sentiment"] / final["Times Spoken"]
    return [final, df]


def metric(string_data):
    metric_type = st.selectbox(
        "Choose analysis type:", ("Overall", "Words", "Time", "Sentiment", "Insights")
    )
    st.header("Total Meeting Breakdown")

    df = parse(string_data)
    total = df[1]
    all_ppl = df[0].Names.unique().tolist()

    ppl = st.multiselect("Participants", options=all_ppl, default=all_ppl)

    if metric_type == "Overall":
        df = df[0][df[0]["Names"].isin(ppl)]
        st.header("Aggregated Overall Breakdown")
        st.dataframe(df)
        st.header("Words Breakdown")
        words(df, ppl)
        st.header("Time Breakdown")
        times(df, ppl)
        st.header("Sentiment Breakdown")
        sentiment(df, ppl)
    elif metric_type == "Words":
        st.header("Words Breakdown")
        words(df[0], ppl)
    elif metric_type == "Time":
        st.header("Time Breakdown")
        times(df[0], ppl)
    elif metric_type == "Sentiment":
        st.header("Sentiment Breakdown")
        sentiment(df[0], ppl)
    else:
        insights(df[0], ppl)


"""
An `InsightFragment` contains the components that make up a meaningful insight.
The attempt was to make a generalisable abstraction rather than resorting to the
crude approach of stacking if conditions on top of another. 

Some degree of success was achieved. The `draft_insight` function contains the 
prototype for what is considered an 'insight'. If you think of the grammatical structure
of an insight, it becomes quite obvious that it is eminently generalisable. 
"""
class InsightFragment:
    """Is the insight consequential or not?"""
    consequential: bool = True

    """
    Who is this insight about? This could very easily have been a tuple of strings.
    But the need was not felt for the intended usage.
    """
    participant: str

    """
    What action is at the center of this insight? The first of the pair is the base verb
    and the second is the past form of the verb/
    """
    verb: tuple[str, str]

    """
    What particular metric is being discussed here?
    """
    kind: str

    """
    This is an anachronism. Althought the attribute is called delta, it may not actually contain
    a delta, in the mathematical sense. It is simply a value upon which decisions may be taken in
    order to prepare insights.
    """
    delta: int

    """
    A word/phrase that constitutes our inference of the '`delta`' being discussed.
    """
    inference: str

    """
    What is the `delta` being compared against?
    """
    benchmark: str

    """
    An addendum that might contain a recommendation based on the nature of that particular insight.
    """
    addendum: Union[str, None]

    """
    What is the nature of the `delta`?
    """
    delta_type: str

    """
    Initialization function for the `InsightFragment` class
    """
    def __init__(
        self,
        participant: str,
        verb: tuple[str, str],
        kind: str,
        delta: int,
        inference: str,
        benchmark: str,
        addendum: Union[str, None],
        delta_type: str,
        consequential: bool = True,
    ) -> None:
        self.participant = participant
        self.verb = verb
        self.kind = kind
        self.delta = delta
        self.inference = inference
        self.benchmark = benchmark
        self.addendum = addendum
        self.delta_type = delta_type


    """
    Drafts the insight from an instance of the `InsightFragment`.

    Additionally, this function also accepts the `inverse_correlation` argument. By default,
    it is set to `True`. It exists to indicate whether the qualitative assessment (e.g. faster, 
    slower) of the `delta` can be understood to be inversely correlated to the modifier we 
    place on the verb (e.g. if 'faster', 'speak slower'). It isn't used now because most insights
    possess an inverse correlation.
    """
    def draft_insight(self, inverse_correlation: bool = True) -> Union[str, None]:
        """
        Prototype for an insight:

        PARTICIPANT VERB DELTA KIND INFERENCE than the BENCHMARK.
        They should consider VERB INFERENCE ADDENDUM.
        """

        formatted_delta = str(round(self.delta, 2))

        # Removing any minus signs as modifiers on the delta will make the nature of 
        # the delta clear.
        formatted_delta = formatted_delta.replace("-", "")
        if self.consequential:
            # The inference is consequential, therefore return an insight.
            return f"{self.participant} {self.verb[1]} {formatted_delta} {self.kind} {self.delta_type} than the {self.benchmark}. They should consider {self.verb[0]}ing {self.inference} {self.addendum}."
        else:
            # The inference is not consequential, do not return an insight.
            return None


def insights(df, ppl):
    df = df[df["Names"].isin(ppl)]
    mean = df["Words"].mean()

    # A tuple of the variables from which insights can be derived. It is at this point
    # that we introduce a decidedly functional turn to our code. This code would have 
    # been infinitely more elegant in a functional language. Python's imperative nature
    # makes the code seem more laborious and unwieldy.
    insightful = [
        (
            # The name of the column in our dataframe with the delta in it.
            "Absolute Mean Variance",

            # The function which calculates the inference for this particular insight.
            lambda x: "less" if x >= 0 else "more",

            # The function which calculates the addendum for this particular insight.
            lambda x: "to let others contribute" if x >= 0 else "to contribute",

            # The function which makes a qualitative assessment of the `delta`.
            lambda x: "more" if x >= 0 else "less",

            # Think of this as the dimension of whatever is being measured.
            "words",

            # What's the benchamrk of this particular dimension?
            "average",

            # The two forms of the verb that at the center of this insight.
            ("speak", "spoke"),

            # A postprocessor to be used.
            lambda x: x,
        ),
        (
            "Sentiment Value",
            lambda x: "on the next step" if x >= 0 else "on their disagreements",
            lambda _: "to progress the conversation",
            lambda x: "which is greater" if x >= 0 else "which is lesser",
            "on the sentiment scale",
            "neutral 0",
            ("reflect", "reflected"),
            lambda x: x.replace("reflected", "rated"),
        ),
        (
            "WPM",
            lambda x: "faster" if x <= 140 else "slower" if x >= 180 else None,
            lambda _: "to remain comprehensible",
            lambda x: "which is less" if x <= 140 else "which is more" if x >= 180 else None,
            "words per minute",
            "advised 140-180 range",
            ("speak", "spoke"),
            lambda x: x,
        ),
    ]
    df["Absolute Mean Variance"] = df["Words"].apply(lambda x: round(x - mean))
    st.header("Insights")
    df_as_dict = df.to_dict("records")

    # Iterate over each name in the dataframe.
    for entry in df_as_dict:
        st.subheader(entry["Names"])

        # Creating our list of pairs, with the first being an `InsightFragment` and
        # the second being a function that takes a string and returns a string.
        insights: List[tuple[InsightFragment, Callable[[str], str]]] = []
        for insightable in insightful:
            # Destructuring our tuple of `insightables`.
            (
                variable,
                inference_func,
                addendum_func,
                observation_func,
                kind,
                benchmark,
                verb,
                postproc,
            ) = insightable
            inference = inference_func(entry[variable])
            addendum = addendum_func(entry[variable])
            delta_type = observation_func(entry[variable])

            if inference:
                # We have a coherent inference to present.
                insights.append(
                    (
                        InsightFragment(
                            participant=entry["Names"],
                            verb=verb,
                            kind=kind,
                            delta=entry[variable],
                            inference=inference,
                            benchmark=benchmark,
                            addendum=addendum,
                            delta_type=delta_type,
                        ),
                        postproc,
                    )
                )

        # Bad practice to create a list that isn't being consumed but we do so
        # in order to iteratively declare our bullet point insights.
        [
            st.markdown(f"* {postproc(insight.draft_insight())}")
            for (insight, postproc) in insights
        ]

def words(df, ppl):
    wordstable = df[df["Names"].isin(ppl)]
    wordstable = wordstable[["Names", "Words"]]

    selectbox = alt.binding_select(
        options=wordstable["Names"].to_numpy(), name="Choose individual to highlight:"
    )

    st.dataframe(wordstable)

    highlight = alt.selection_single(fields=["Names"], bind=selectbox)
    color = alt.condition(highlight, alt.value("#FF4B4B"), alt.value("lightgray"))

    wordchart = (
        alt.Chart(wordstable)
        .mark_bar()
        .encode(
            alt.X("Names", axis=alt.Axis(title="Names", grid=False)),
            alt.Y("Words", axis=alt.Axis(title="Words", grid=False)),
            color=color,
            tooltip=[alt.Tooltip("Words:Q", title="Words Spoken")],
        )
        .add_selection(highlight)
        .properties(title="Words Spoken", height=450)
        .interactive()
    )

    rule = (
        alt.Chart(wordstable)
        .mark_rule(color="black", size=5, opacity=0.2)
        .encode(y="mean(Words)")
    )

    st.altair_chart(wordchart + rule, use_container_width=True)


def times(df, ppl):
    timetable = df[df["Names"].isin(ppl)]
    timetable = timetable[["Names", "Time Spoken (seconds)", "WPM"]]

    selectbox = alt.binding_select(
        options=timetable["Names"].to_numpy(), name="Choose individual to highlight:"
    )
    highlight = alt.selection_single(fields=["Names"], bind=selectbox)
    color = alt.condition(highlight, alt.value("#FF4B4B"), alt.value("lightgray"))

    st.dataframe(timetable)

    for i in range(2):
        if i == 1:
            input_string = "Time Spoken (seconds)"
            remote_string = "Time (s)"
        else:
            input_string = "WPM"
            remote_string = "WPM"

        if input_string == "Time Spoken (seconds)":
            rule = (
                alt.Chart(timetable)
                .mark_rule(color="black", size=5, opacity=0.2)
                .encode(
                    y="mean(Time Spoken (seconds))",
                )
            )
        else:
            rule = (
                alt.Chart(pd.DataFrame({"y": [190]}))
                .mark_rule(strokeDash=[10, 10], color="black", size=5, opacity=0.2)
                .encode(y="y")
            )

        timechart = (
            alt.Chart(timetable)
            .mark_bar()
            .encode(
                alt.X("Names", axis=alt.Axis(title="Names", grid=False)),
                alt.Y(input_string, axis=alt.Axis(title=remote_string, grid=False)),
                color=color,
                tooltip=[alt.Tooltip(input_string, title=input_string)],
            )
            .add_selection(highlight)
            .properties(title=input_string, height=550)
            .interactive()
        )

        st.altair_chart(timechart + rule, use_container_width=True)

def sentiment(df, ppl):
    sentimentTable = df[df["Names"].isin(ppl)]
    sentimentTable = sentimentTable[["Names", "Sentiment Value"]]
    selectbox = alt.binding_select(
        options=sentimentTable["Names"].to_numpy(),
        name="Choose individual to highlight:",
    )
    highlight = alt.selection_single(fields=["Names"], bind=selectbox)
    color = alt.condition(highlight, alt.value("#FF4B4B"), alt.value("lightgray"))
    sentimentGraph = (
        alt.Chart(sentimentTable)
        .mark_bar()
        .encode(
            alt.X("Names", axis=alt.Axis(title="Names", grid=False)),
            alt.Y("Sentiment Value", axis=alt.Axis(title="Sentiment", grid=False)),
            color=color,
            tooltip=[alt.Tooltip("Sentiment Value:Q", title="Sentiment")],
        )
        .add_selection(highlight)
        .properties(title="Sentiment", height=450)
        .interactive()
    )

    st.dataframe(sentimentTable)
    st.altair_chart(sentimentGraph, use_container_width=True)


def app():
    st.header("Metrics & Insights")
    text = st.text("In the navigation bar on the left, please upload the transcript.")
    with st.sidebar.header("Upload your file"):
        uploaded_file = st.sidebar.file_uploader(
            "Please upload a file of type: vtt", type="vtt"
        )
    if uploaded_file is not None:
        text = st.text(
            "Please wait for analysis to complete. Once ready, metrics will appear below. \nSelect 'Insights' for further information."
        )
        bytes_data = uploaded_file.getvalue()
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # To read file as string:
        string_data = stringio.read()
        if "cached_corpus" not in st.session_state:
            st.session_state["cached_corpus"] = string_data
        metric(string_data)
    else:
        # This is a bad idea because we're essentially recomputing
        # the results for each time a tab switch happens. But the
        # difference should be fairly miniscule on modern machines.
        string_data = st.session_state.get("cached_corpus")
        if string_data:
            metric(string_data)
        else:
            pass


