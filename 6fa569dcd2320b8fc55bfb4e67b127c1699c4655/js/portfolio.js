angular.module('portfolioApp', [])
.controller('navController', function () {
  var navList = this;
  navList.list = [
    {menu:"Home", nav:"index.html"},
    {menu:"Projects", nav:"projects.html"},
    {menu:"Case Studies", nav:"case-studies.html"},
  ];
})

.controller('portController', function () {
  var portList = this;
  portList.list = [
    {gallery: "gallery-design.html", thumbnail:"hub-design", figcaption:"Gallery of Design Projects"},
    {gallery: "gallery-development.html", thumbnail:"hub-develop", figcaption:"Gallery of Development Projects"},
    {gallery: "case-studies.html", thumbnail:"hub-teach", figcaption:"Gallery of Case Studies"},
    {gallery: "gallery-think.html", thumbnail:"hub-think", figcaption:"Gallery of Projects for Fun"},
  ];
})

.controller('caseController', function () {
  var caseList = this;
  caseList.list = [
    {study: "case-study-mgm-production-services.html", thumbnail:"hub-case-study-mgm", figcaption:"MGM Production Services"},
    {study: "case-study-adventuredome.html", thumbnail:"hub-case-study-adventuredome", figcaption:"Adventuredome"},
  ];
})

.controller('galleryController', function () {
  var galleryList = this;
  galleryList.list = [
    {id:"1", image:"design-aria-dining"},
    {id:"2", image:"design-julian"},
    {id:"3", image:"design-production-services-mobile"},
    {id:"4", image:"design-tringling-logo"},
    {id:"5", image:"design-tringling-webapp"},
    {id:"6", image:"design-tringling-bc"},
    {id:"7", image:"design-production-services"},
    {id:"8", image:"design-mlife"}
  ];
})
