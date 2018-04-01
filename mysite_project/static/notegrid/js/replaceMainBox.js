var mainpage = document.getElementById('mainpage');
mainpageParent = mainpage.parentNode;
mainpageParent.removeChild(mainpage);
var newBody = document.createElement('div');
newBody.id = 'chartDiv';
mainpageParent.appendChild(newBody);
