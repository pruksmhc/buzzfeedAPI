Skip to content
This repository  
Search
Pull requests
Issues
Gist
 @pruksmhc
 Watch 1
  Star 1
 Fork 1 radiodario/brandwatch-wordcloud
 Code  Issues 0  Pull requests 0  Wiki  Pulse  Graphs
Branch: master Find file Copy pathbrandwatch-wordcloud/src/wordcloud.js
ec302a7  on Dec 1, 2014
@radiodario radiodario use roboto so that IE11 doesn't look crap
1 contributor
RawBlameHistory     119 lines (93 sloc)  2.57 KB
var d3 = require('d3');
// we use Jason Davies' wordcloud layout.
d3.layout.cloud = require('d3.layout.cloud/d3.layout.cloud');

// data -- this would be a query or a promise or whatever on
// a real application
var topics = require('./topics.json').topics;
// find out what the maximum volume is
var maxVolume = d3.max(topics, function(d) {return d.volume});

// function that steps up the fontSize
function fontSize(topic) {
  var step = maxVolume / 6 | 0; // six different fontSizes
  var fontSize = 14;
  var sizeStep = 11;
  var volume = topic.volume;
  var search = 0;
  while (search < volume) {
    search += step;
    fontSize += sizeStep;
  }

  topic.fontSize = fontSize;
}

// set the fontsize on each
topics.map(fontSize);



module.exports = {

  clickHandler: null,


  init: function (domNode, clickHandler) {


    this.svg = d3.select(domNode).select("svg");
    this.clickHandler = clickHandler;


    // XXX make responsive
    this.w = 800;
    this.h = 600

    this.layout = d3.layout.cloud()
      .size([this.w, this.h]) // some random size
      .words(topics)
      .text(function(d) {
        return d.label;
      })
      .font("Roboto")
      .fontSize(function(d) {
        return d.fontSize;
      })
      .rotate(0)
      .on("end", this.draw.bind(this)) // UGLY! ;_;
      .start();
  },

  draw: function (words) {



    this.svg
      .attr("width", this.w)
      .attr("height", this.h);


    var terms = this.svg.append("g")
      .attr("transform", "translate(" + this.w/2 + "," + this.h/2 + ")")
      .selectAll("text")
        .data(words)

    terms
      .enter()
        .append("text")
        .attr("class", "term")
        .style("font-family", "Roboto")
        .style("font-size", function(d) {
          return d.size + "px";
        })
        .style("fill", function(d) {
          if (d.sentimentScore < 40) {
            // red
            return "#D84315";
          } else if (d.sentimentScore > 60) {
            // green
            return "#4CAF50";
          } else {
            // grey
            return "hsl(250, 20%, 80%)";
          }
        })
        .attr("text-anchor", "middle")
        .attr("fill-opacity", 0)
        .text(function(d) {
          return d.label;
        })
        .on('click', this.clickHandler)

    // animate the terms entering
    // so that it looks nicer
    terms
      .transition()
      .delay(function(d, i) {
        return 100 * i;
      })
      .duration(100)
      .attr("fill-opacity", 1)
      .attr("transform", function(d) {
        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
      });

  }

};
Status API Training Shop Blog About Pricing
© 2015 GitHub, Inc. Terms Privacy Security Contact Help