const menu = document.querySelector("#menu__btn");
const navbar = document.querySelector(".navbar");

menu.onclick = () => {
  menu.classList.toggle("fa-times");
  navbar.classList.toggle("active");
};

window.onscroll = () => {
  menu.classList.remove("fa-times");
  navbar.classList.remove("active");
};

// Smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth"
    });
  });
});

// Form validation
document.querySelector("form").addEventListener("submit", function (e) {
  const name = document.querySelector('input[placeholder="Name"]').value;
  const number = document.querySelector('input[placeholder="Number"]').value;
  const email = document.querySelector('input[placeholder="Email"]').value;
  const date = document.querySelector('input[type="date"]').value;

  if (!name || !number || !email || !date) {
    e.preventDefault();
    alert("Please fill in all fields.");
  } else {
    e.preventDefault();
    alert(`Appointment booked successfully!\n\nDetails:\nName: ${name}\nNumber: ${number}\nEmail: ${email}\nDate: ${date}`);
  }
});

// Back to top button
const backToTopButton = document.createElement("button");
backToTopButton.innerHTML = "↑";
backToTopButton.id = "backToTop";
backToTopButton.style.position = "fixed";
backToTopButton.style.bottom = "40px";
backToTopButton.style.right = "40px";
backToTopButton.style.padding = "20px";
backToTopButton.style.border = "none";
backToTopButton.style.borderRadius = "5px";
backToTopButton.style.backgroundColor = "#1b9c85";
backToTopButton.style.color = "#fff";
backToTopButton.style.cursor = "pointer";
backToTopButton.style.display = "none";
document.body.appendChild(backToTopButton);

backToTopButton.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
});

window.addEventListener("scroll", () => {
  if (window.scrollY > 300) {
    backToTopButton.style.display = "block";
  } else {
    backToTopButton.style.display = "none";
  }
});