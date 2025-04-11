// main.js
$(document).ready(function() {
    // Ao clicar em "Pessoas" no menu, carregamos pessoa.html
    $("#linkPessoas").click(function(e) {
      e.preventDefault();
      $("#divPrincipal").load("/view/pessoa", function() {
        // Após carregar o HTML, carregamos o script do CRUD
        $.getScript("JS/pessoa.js")
          .done(function() {
            // Inicializa os eventos e carrega a lista de pessoas            
          })
          .fail(function() {
            console.error("Não foi possível carregar pessoa.js");
          });
      });
    });
  });
  