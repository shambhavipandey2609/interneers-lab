import React from "react";
import { Product } from "../types";

interface Props {
  product: Product;
  onEdit: (product: Product) => void;
  isExpanded: boolean;
  onToggle: () => void;
}

const ProductCard: React.FC<Props> = ({
  product,
  onEdit,
  isExpanded,
  onToggle,
}) => {
  return (
    <div
      style={{
        border: "1px solid #ccc",
        padding: "1rem",
        marginBottom: "1rem",
        borderRadius: "8px",
        background: "#f9f9f9",
        cursor: "pointer",
      }}
      onClick={onToggle}
    >
      <h2>{product.name}</h2>
      <p>
        <strong>Price:</strong> ₹{product.price}
      </p>

      {isExpanded && (
        <>
          <p>
            <strong>Description:</strong> {product.description}
          </p>
          <p>
            <strong>Category:</strong> {product.category}
          </p>
        </>
      )}

      {/* Prevent bubbling to card click */}
      <button
        onClick={(e) => {
          e.stopPropagation();
          onEdit(product);
        }}
        style={{ marginTop: "0.5rem" }}
      >
        Edit
      </button>
    </div>
  );
};

export default ProductCard;
