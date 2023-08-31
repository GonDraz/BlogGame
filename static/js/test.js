const btnSwitch = document.getElementsByClassName("nav-link");
console.log("This is a JavaScript log message.");
btnSwitch.addEventListener("click", () => {
  const currentTheme = document.documentElement.getAttribute("data-bs-theme");
  if (currentTheme === "dark") {
    document.documentElement.setAttribute("data-bs-theme", "light");
    localStorage.setItem("data-bs-theme", "light");
  } else {
    document.documentElement.setAttribute("data-bs-theme", "dark");
    localStorage.setItem("data-bs-theme", "dark");
  }
});

// Set initial theme based on local storage
const savedTheme = localStorage.getItem("data-bs-theme");
if (savedTheme) {
  document.documentElement.setAttribute("data-bs-theme", savedTheme);
}
