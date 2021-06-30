
  function checkMbps(){
    event.preventDefault();
    var x = document.getElementById("zapis_u_speed").querySelectorAll(".u_prep");
    var y = document.getElementById("zapis_d_speed").querySelectorAll(".d_prep");
   
    if(document.getElementById("result-unit").innerHTML=="Kb/s") {
      $("#result_box").empty();
      $("#result_box").prepend(`<span id="result-unit" style="color:black;font-weight:normal;font-style: italic;">Mb/s</span>`);

      for (let i = 0; i < x.length; i++) {
        var u_speed_i="u_speed"+(x.length-i-1);
        console.log(u_speed_i)
        $("#"+u_speed_i).html(((x[i].innerHTML))/1000);
      }
      for (let i = 0; i < y.length; i++) {
        var d_speed_i="d_speed"+(y.length-i-1);
        console.log(d_speed_i)
        $("#"+d_speed_i).html(((y[i].innerHTML))/1000);
      }
    }
  }

  function checkKbps(){
    event.preventDefault();
    var x = document.getElementById("zapis_u_speed").querySelectorAll(".u_prep");
    var y = document.getElementById("zapis_d_speed").querySelectorAll(".d_prep");
    if(document.getElementById("result-unit").innerHTML=="Mb/s") {
      $("#result_box").empty();
      $("#result_box").prepend(`<span id="result-unit" style="color:black;font-weight:normal;font-style: italic;">Kb/s</span>`);

      for (let i = 0; i < x.length; i++) {
        var u_speed_i="u_speed"+(x.length-i-1);
        console.log(u_speed_i)
        $("#"+u_speed_i).html((x[i].innerHTML)*1000);
      }
      for (let i = 0; i < y.length; i++) {
        var d_speed_i="d_speed"+(y.length-i-1);
        console.log(d_speed_i)
        $("#"+d_speed_i).html(((y[i].innerHTML))*1000);
      }
    }
  }
