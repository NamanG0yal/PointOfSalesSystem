# Inventory System Models Documentation

This documentation outlines the models for an inventory management system, including **InventoryItem**, **Customer**, **Staff**, and **Transaction** models. Each section covers field descriptions, relationships, and example usage for interacting with the system.

---

## **1. InventoryItem Model**

### **Fields**:
- **`Item_SKU`** (`VARCHAR(50)`):  
  The **Stock Keeping Unit** (SKU) uniquely identifies each product in the inventory. This field serves as the **primary key** for the model.  
  Example: `SKU12345`

- **`Item_Name`** (`VARCHAR(100)`):  
  The name of the product.  
  Example: `Laptop`

- **`Item_Description`** (`TEXT`):  
  A detailed description of the product.  
  Example: `14-inch display laptop with Intel i7 processor, 16GB RAM, 512GB SSD.`

- **`Item_Price`** (`DECIMAL(10, 2)`):  
  The price of the product, stored as a decimal value with two digits after the decimal point.  
  Example: `1999.99`

- **`Item_Qty`** (`INTEGER`):  
  The quantity of the product available in the inventory.  
  Example: `50`

### **Relationships**:
- **No direct relationships** to other models. However, it is indirectly related to the **Transaction** model via the products involved in transactions.

### **Example Usage**:

```sql
-- Insert a new inventory item
INSERT INTO inventory_items (Item_SKU, Item_Name, Item_Description, Item_Price, Item_Qty)
VALUES ('SKU12345', 'Laptop', '14-inch display laptop with Intel i7 processor, 16GB RAM, 512GB SSD.', 1999.99, 50);

-- Query to get all products in the inventory
SELECT * FROM inventory_items;

-- Update an item's quantity
UPDATE inventory_items
SET Item_Qty = Item_Qty - 1
WHERE Item_SKU = 'SKU12345';

-- Query to find a product by SKU
SELECT * FROM inventory_items WHERE Item_SKU = 'SKU12345';