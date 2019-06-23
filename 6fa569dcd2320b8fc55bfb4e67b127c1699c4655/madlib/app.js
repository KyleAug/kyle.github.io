var data;
var txt = "&ndash; I'm Sabastian Shaw. <br>&ndash; I'm Jean @@Silly-Word@@. <br>&ndash; Let's make this quick, I only have @@Amount-of-Time@@. <br>&ndash; This interview is for the special '@@Holiday@@ issue' of the newspaper. You are very @@Adjective@@ to amassed such an empire. To what do you owe your success? <br>&ndash; I follow the same routine every morning. I'm waking up, brushing  my teeth, then @@Verb-(ending-in-ing)@@ at the gym. <br>&ndash; Your company is involved primarily in agricultural projects feeding the world's @@Animal-(plural)@@. With that type of passion, I wonder if your @@Body-Part@@ might be bigger than you let on. <br>&ndash; Some people say I don't have a @@Body-Part@@ at all. <br>&ndash; I did some research on you and I see you're unmarried and you were adopted at age @@Number@@. <br>&ndash; You intrigue me, Miss @@Silly-Word@@. When someone addresses me, I @@Verb@@ like sesame.<br>&ndash; My @@Article-of-Clothing@@ is sweating. <br>&ndash; What are your plans after you graduate? <br>&ndash; I was planning on moving to @@City@@ with @@Name-of-Celebrity@@. <br>&ndash; The best part about having success is giving advice to students like you. @@Song-Lyric@@. <br>&ndash; When I'm around you, I feel like a @@Profession@@ at a @@Type-of-Event@@. <br>&ndash; You know. I heard that before. I hope that you have everything you need. <br>&ndash;  I do. Whenever I have a great interview, I do my favorite dance called the @@Adjective@@ @@Food@@. <br>@@Excamation@@.";

function setup() {
  noCanvas()
  Tabletop.init( { key: '1q4UYOYuBlGADej91SS-mB_PFDtaJsjPyT0DmWGC1L84',
                     callback: gotData,
                     simpleSheet: true } )

  var button = document.createElement('button')
  button.innerHTML = 'Generate Madlib';
  var bodyP = document.getElementsByTagName('p')[0];
  bodyP.appendChild(button);
  button.addEventListener('click', generateData)
}


  function replacer(match, madData) {
    var entry = random(data)
    return entry[madData]

  }


    function generateData() {
      var madLib = txt.replace(/@@(.*?)@@/gi, replacer)
      var bodyP0 = document.getElementsByTagName('p')[1]
      bodyP0.innerHTML = madLib
    }

    function gotData(stuff, tabletop) {
      data = stuff
    }
