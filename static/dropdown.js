/* When the user clicks on the button, 
    toggle between hiding and showing the dropdown content */
 
  
  
  
  function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }


  function deleteFja() {
    document.getElementById("dropDelete").classList.toggle("show");
  }
  function mjJedFunc() {
    document.getElementById("mj_jed").classList.toggle("show");
  }

  // Close the dropdown if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.filterbtn')&&document.getElementById('myDropdown').className=="dropdown-content show") {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
    if (!event.target.matches('.deletebtn')&&document.getElementById('dropDelete').className=="dropdown-content show") {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
    if (!event.target.matches('.measubtn')&&document.getElementById('mj_jed').className=="dropdown-content show") {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }
  
  
      