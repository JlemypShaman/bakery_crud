const form = document.getElementById("productForm");
const table = document.getElementById("productTable");

async function loadProducts() {
  const res = await fetch("/products");
  const data = await res.json();
  table.innerHTML = data.map(p => `
    <tr>
      <td>${p.id}</td>
      <td>${p.name}</td>
      <td>${p.description || ""}</td>
      <td>${p.price.toFixed(2)} zł</td>
      <td>${p.baked_date}</td>
      <td>${p.ingredients || ""}</td>
      <td>${p.is_gluten_free ? "Tak" : "Nie"}</td>
      <td><button class="btn btn-sm btn-danger" onclick="deleteProduct(${p.id})">Usuń</button></td>
    </tr>
  `).join("");
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const product = {
    name: form.name.value,
    description: form.description.value,
    price: parseFloat(form.price.value),
    baked_date: form.baked_date.value,
    ingredients: form.ingredients.value,
    is_gluten_free: form.is_gluten_free.checked
  };
  await fetch("/products", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(product)
  });
  form.reset();
  loadProducts();
});

async function deleteProduct(id) {
  await fetch(`/products/${id}`, { method: "DELETE" });
  loadProducts();
}

loadProducts();
