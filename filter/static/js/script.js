const searchForm = document.getElementById("search-form");
const searchBtn = document.getElementById("search-btn");

searchBtn.addEventListener("click", function (event) {
  searchForm.submit();
});
