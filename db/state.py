

class Service(object):
    content = {}


    def __init__(self,content):
        """arguments:service, heading2, heading3, paragraphs """
        self.content = content
        self.content = {
            "Mechanical": {
                "1.1": {
                    "heading" : "FCUs",
                    "para": "blblbl blbl blblb blblb"
                },
                "1.2": {
                    "heading": "Chilled Beams",
                    "para": "blab blab blab blab"
                }
            },
            "Hydraulics": {
                "1.1": {
                    "heading" : "Pipes",
                    "para": "blblbl blbl blblb blblb"
                },
                "1.2": {
                    "heading": "Pipes2",
                    "para": "blab blab blab blab"
                }
            },
            "Electrical": {
                "1.1": {
                    "heading" : "lights",
                    "para": "blblbl blbl blblb blblb"
                },
                "1.2": {
                    "heading": "conduits",
                    "para": "blab blab blab blab"
                }
            },
            "ICT": {
                "1.1": {
                    "heading" : "TV",
                    "para": "blblbl blbl blblb blblb"
                },
                "1.2": {
                    "heading": "conduits",
                    "para": "blab blab blab blab"
                }
            }

        }
