document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Evitar que el formulario se envíe
  
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
  
    if (username!== null && password!== null) {
      alert("Inicio de sesión exitoso");
      // Aquí puedes redirigir al usuario a otra página o realizar acciones adicionales
    } else {
      var errorElement = document.createElement("p");
      errorElement.className = "error";
      errorElement.textContent = "Credenciales inválidas";
      document.getElementById("loginForm").appendChild(errorElement);
    }
  });