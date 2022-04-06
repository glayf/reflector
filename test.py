from seleniumbase import BaseCase

class MyTestClass(BaseCase):
    def test_sidebar(self):
        self.open("http://localhost:8501")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-sygy1k.e1fqkh3o1 > div.css-1f7vzus.e1fqkh3o2 > button > svg")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-qpy8u8.e1fqkh3o3 > button")
        self.assert_element("#root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-sygy1k.e1fqkh3o1 > div.css-1f7vzus.e1fqkh3o2 > button > svg")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-sygy1k.e1fqkh3o1")


    def test_intro(self):
        self.open("http://localhost:8501")
        self.assert_element("#welcome-to-reflector")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.egzxvld1 > div > div:nth-child(1) > div > div.css-1fcdlhc.e1s6o5jp0 > ul > li > div.streamlit-expanderHeader.st-ae.st-bp.st-ag.st-ah.st-ai.st-aj.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw.st-as.st-at.st-bx.st-by.st-bz.st-c0.st-c1.st-b4.st-c2.st-c3.st-c4.st-b5.st-c5.st-c6.st-c7.st-c8 > svg")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.egzxvld1 > div > div:nth-child(1) > div > div.css-1fcdlhc.e1s6o5jp0 > ul > li > div.streamlit-expanderHeader.st-ae.st-bp.st-ag.st-ah.st-ai.st-aj.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw.st-as.st-at.st-bx.st-by.st-bz.st-c0.st-df.st-b4.st-c2.st-c3.st-c4.st-b5.st-c5.st-c6.st-c7.st-c8")
        self.assert_element("#root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.egzxvld1 > div > div:nth-child(1) > div > div.css-1fcdlhc.e1s6o5jp0 > ul > li > div.streamlit-expanderContent.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-bs.st-bq.st-ce.st-cf.st-bv.st-bw.st-as.st-at.st-bx.st-by.st-bz.st-c0.st-c1.st-cg.st-am.st-ch.st-ci.st-b1.st-cj.st-b3.st-c6.st-c7.st-c8 > div:nth-child(1) > div > div:nth-child(1) > div")
        self.assert_element("#root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.egzxvld1 > div > div:nth-child(1) > div > div.css-1fcdlhc.e1s6o5jp0 > ul > li > div.streamlit-expanderContent.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-bs.st-bq.st-ce.st-cf.st-bv.st-bw.st-as.st-at.st-bx.st-by.st-bz.st-c0.st-c1.st-cg.st-am.st-ch.st-ci.st-b1.st-cj.st-b3.st-c6.st-c7.st-c8 > div:nth-child(1) > div > div:nth-child(5) > div")
        

    def test_upload(self):
        self.open("http://localhost:8501")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-sygy1k.e1fqkh3o1 > div.block-container.css-128j0gw.egzxvld2 > div:nth-child(1) > div > div:nth-child(2) > div > div > label:nth-child(2) > div.st-d3.st-dc.st-bq.st-ae.st-af.st-ag.st-ah.st-ai.st-aj")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-sygy1k.e1fqkh3o1 > div.block-container.css-128j0gw.egzxvld2 > div:nth-child(1) > div > div:nth-child(4) > div > section > button")
        self.sleep(5)


    def test_metrics(self):
        self.open("http://localhost:8501")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-sygy1k.e1fqkh3o1 > div.block-container.css-128j0gw.egzxvld2 > div:nth-child(1) > div > div:nth-child(2) > div > div > label:nth-child(2) > div.st-d3.st-dc.st-bq.st-ae.st-af.st-ag.st-ah.st-ai.st-aj")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-sygy1k.e1fqkh3o1 > div.block-container.css-128j0gw.egzxvld2 > div:nth-child(1) > div > div:nth-child(4) > div > section > button")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.egzxvld1 > div > div:nth-child(1) > div > div.css-1fcdlhc.e1s6o5jp0 > ul > li")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.egzxvld1 > div > div:nth-child(1) > div > div.css-1fcdlhc.e1s6o5jp0 > ul > li")
        self.sleep(2)
        self.click("#root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.egzxvld1 > div > div:nth-child(1) > div > div:nth-child(13) > div > div > div > form > div > label > select")
        self.click("#aggregated-overall-breakdown")
        self.assert_element("#aggregated-overall-breakdown")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.egzxvld1 > div > div:nth-child(1) > div > div:nth-child(5) > div > div > div")
        self.click("#aggregated-overall-breakdown")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.egzxvld1 > div > div:nth-child(1) > div > div:nth-child(13) > div > div > details > summary > svg")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.egzxvld1 > div > div:nth-child(1) > div > div:nth-child(13) > div > div > details > div > a:nth-child(2)")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-sygy1k.e1fqkh3o1 > div.block-container.css-128j0gw.egzxvld2 > div:nth-child(1) > div > div:nth-child(2) > div > div > label:nth-child(3) > div.st-d3.st-dc.st-bq.st-ae.st-af.st-ag.st-ah.st-ai.st-aj")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-sygy1k.e1fqkh3o1 > div.css-1f7vzus.e1fqkh3o2 > button > svg > path")
        self.assert_element("#help-key > div > span")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-qpy8u8.e1fqkh3o3 > button > svg > path")
        self.click("#root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-sygy1k.e1fqkh3o1 > div.block-container.css-128j0gw.egzxvld2 > div:nth-child(1) > div > div:nth-child(2) > div > div > label:nth-child(2) > div.st-d3.st-dc.st-bq.st-ae.st-af.st-ag.st-ah.st-ai.st-aj")
        self.assert_element("#total-meeting-breakdown > div > span")
        self.assert_element("#insights > div > span")