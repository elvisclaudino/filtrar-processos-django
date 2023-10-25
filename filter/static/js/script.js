const searchForm = document.getElementById("search-form"); // Seleciona o formulário de busca
const searchBtn = document.getElementById("search-btn"); // Seleciona o botão de busca

searchBtn.addEventListener("click", function (event) {
  // Adiciona um evento de clique ao botão de busca
  searchForm.submit(); // Submete o formulário de busca
});
