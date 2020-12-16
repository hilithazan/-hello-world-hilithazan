function UpdateFun(){
    var d =new Date();
    var months = ["January","February", "March" ,"April", "May", "June", "July", "August", "September", "October","November", "December"];
    document.getElementById("IMGDate").innerHTML=months[d.getMonth()] +", " +d.getFullYear();
  }

  function RcivedComment () {
    document.getElementById("Submit").innerHTML="Thank you! Your comment has been recived"
}
