const addBookingBtn = document.querySelector('#bookings button');

addBookingBtn.addEventListener('click', () => {
  // code to open the booking form
});
const editBtns = document.querySelectorAll('button[type="edit"]');

editBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    // code to open the editing form for this booking or customer
  });
});
const deleteBtns = document.querySelectorAll('button[type="delete"]');

deleteBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    // code to delete this booking or customer from the table
  });
});
const navLinks = document.querySelectorAll('nav a');
const sections = document.querySelectorAll('main section');

navLinks.forEach(link => {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    const sectionId = link.getAttribute('href');
    const sectionToShow = document.querySelector(sectionId);
    sections.forEach(section => section.style.display = 'none');
    sectionToShow.style.display = 'block';
  });
});
