function buildpiechart(countryname) {

    d3.select("#pieChart").html("")
        // d3.select("body")
        .append("pieChart")
    d3.json("https://raw.githubusercontent.com/melvinabraham/AustralianOpen_Visualization/master/data/Countries/" + countryname + ".json", function (error, data) {
        var array = []
        var json_content = { "content": array };
        for (var i = 0; i < data.length; ++i) {
            var name = data[i][0];
            var score = data[i][1];
            var color = '#' + (0x1000000 + (Math.random()) * 0xffffff).toString(16).substr(1, 6);
            json_content.content.push({ "label": name, "value": score, "color": color });
        }

        var pie = new d3pie("pieChart", {
            "header": {
                "title": {
                    "text": "Player Performance",
                    "fontSize": 22,
                    "font": "verdana"
                },
                "subtitle": {
                    "text": "Performance of every player in " + countryname,
                    "color": "#999999",
                    "fontSize": 10,
                    "font": "verdana"
                },
                "titleSubtitlePadding": 12
            },
            "footer": {
                "text": "How every player performs against his fellow countrymen.",
                "color": "#999999",
                "fontSize": 11,
                "font": "open sans",
                "location": "bottom-center"
            },
            "size": {
                "canvasHeight": 400,
                "canvasWidth": 590,
                "pieOuterRadius": "88%"
            },
            "data": json_content,
            "labels": {
                "outer": {
                    "pieDistance": 32
                },
                "inner": {
                    "format": "value"
                },
                "mainLabel": {
                    "font": "verdana"
                },
                "percentage": {
                    "color": "#e1e1e1",
                    "font": "verdana",
                    "decimalPlaces": 0
                },
                "value": {
                    "color": "#e1e1e1",
                    "font": "verdana"
                },
                "lines": {
                    "enabled": true,
                    "color": "#cccccc"
                },
                "truncation": {
                    "enabled": true
                }
            },
            "effects": {
                "pullOutSegmentOnClick": {
                    "effect": "linear",
                    "speed": 400,
                    "size": 8
                }
            }
        });

    });
}