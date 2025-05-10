import React, { useState } from "react";
import { Routes, Route, useNavigate, useParams } from "react-router-dom";
import ProductCard from "./components/ProductCard";
import ProductEdit from "./components/ProductEdit";
import { Product } from "./types";

// Define initial products with valid string category values
const initialProducts: Product[] = [
  {
    id: 1,
    name: "Monitor",
    price: 8000,
    description: "24-inch full HD LED monitor.",
    category: "Electronics", // Ensure category is always a string
  },
  {
    id: 2,
    name: "Mouse",
    price: 500,
    description: "Ergonomic wireless mouse.",
    category: "Electronics", // Ensure category is always a string
  },
  {
    id: 3,
    name: "Keyboard",
    price: 1000,
    description: "Mechanical keyboard with RGB lights.",
    category: "Electronics", // Ensure category is always a string
  },
];

// ProductList component to display all products
const ProductList: React.FC<{
  products: Product[];
  onEdit: (product: Product) => void;
}> = ({ products, onEdit }) => {
  const [selectedProductId, setSelectedProductId] = useState<number | null>(
    null,
  );

  const toggleProduct = (productId: number) => {
    setSelectedProductId((prevId) => (prevId === productId ? null : productId));
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Product List</h1>
      {products.map((product) => (
        <div key={product.id}>
          <ProductCard
            product={product}
            onEdit={() => onEdit(product)}
            isExpanded={selectedProductId === product.id}
            onToggle={() => toggleProduct(product.id)}
          />
        </div>
      ))}
    </div>
  );
};

// ProductEditWrapper component to handle editing the selected product
const ProductEditWrapper: React.FC<{
  products: Product[];
  onSave: (updatedProduct: Product) => void;
}> = ({ products, onSave }) => {
  const { productId } = useParams();
  const navigate = useNavigate();

  const product = products.find((p) => p.id === Number(productId));
  if (!product) return <div>Product not found</div>;

  return (
    <ProductEdit
      product={product}
      onSave={(updated) => {
        onSave(updated);
        navigate("/"); // Navigate back to the product list after saving
      }}
    />
  );
};

// Main App component
const App: React.FC = () => {
  const [products, setProducts] = useState<Product[]>(initialProducts);
  const navigate = useNavigate();

  const handleSave = (updatedProduct: Product) => {
    setProducts((prev) =>
      prev.map((p) => (p.id === updatedProduct.id ? updatedProduct : p)),
    );
  };

  return (
    <Routes>
      <Route
        path="/"
        element={
          <ProductList
            products={products}
            onEdit={(product) => navigate(`/product/${product.id}`)}
          />
        }
      />
      <Route
        path="/product/:productId"
        element={<ProductEditWrapper products={products} onSave={handleSave} />}
      />
    </Routes>
  );
};

export default App;
