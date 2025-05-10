import React, { useState } from "react";
import { Product } from "../types";

const ProductEdit: React.FC<{
  product: Product;
  onSave: (updatedProduct: Product) => void;
}> = ({ product, onSave }) => {
  const [name, setName] = useState(product.name);
  const [price, setPrice] = useState(product.price);
  const [description, setDescription] = useState(product.description);
  const [category, setCategory] = useState(product.category);
  const [error, setError] = useState<string | null>(null);

  // Price validation
  const handlePriceChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newPrice = parseFloat(e.target.value);
    setPrice(newPrice);

    if (newPrice < 0) {
      setError("Price cannot be negative");
    } else {
      setError(null);
    }
  };

  // Handle change for other fields
  const handleNameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setName(e.target.value);
  };

  const handleDescriptionChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setDescription(e.target.value);
  };

  const handleCategoryChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setCategory(e.target.value);
  };

  // Handle Save
  const handleSave = () => {
    if (!error) {
      onSave({ id: product.id, name, price, description, category });
    }
  };

  return (
    <div>
      <h1>Edit Product</h1>
      <div>
        <label>
          Name:
          <input type="text" value={name} onChange={handleNameChange} />
        </label>
      </div>
      <div>
        <label>
          Price:
          <input type="number" value={price} onChange={handlePriceChange} />
        </label>
        {error && <p style={{ color: "red" }}>{error}</p>}
      </div>
      <div>
        <label>
          Description:
          <input
            type="text"
            value={description}
            onChange={handleDescriptionChange}
          />
        </label>
      </div>
      <div>
        <label>
          Category:
          <input type="text" value={category} onChange={handleCategoryChange} />
        </label>
      </div>
      <button onClick={handleSave}>Save</button>
    </div>
  );
};

export default ProductEdit;
