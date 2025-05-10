document.addEventListener("DOMContentLoaded", function () {
  // Get the place where we want to show products
  let container = document.getElementById("product-container");

  // Fetch products from the backend
  fetch("http://localhost:8000/api/new-products/")
    .then(function (response) {
      return response.json(); // Convert response to JS object
    })
    // products variable holds the list of product objects.
    .then(function (products) {
      // Show each product one by one
      for (let i = 0; i < products.length; i++) {
        let product = products[i];

        // Create a box for the product
        let box = document.createElement("div");
        box.className = "product-tile";

        // Add product details inside the box
        box.innerHTML =
          "<h3>" +
          product.name +
          "</h3>" +
          "<p>" +
          product.description +
          "</p>" +
          "<p><strong>Price:</strong> ₹" +
          product.price +
          "</p>" +
          "<p><strong>Category:</strong> " +
          product.category +
          "</p>" +
          "<p><strong>Brand:</strong> " +
          product.brand +
          "</p>" +
          "<p><strong>Stock:</strong> " +
          product.stock +
          "</p>";

        // Add the box to the page
        container.appendChild(box);
      }
    })
    .catch(function (error) {
      console.log("Error loading products:", error);
    });
});
