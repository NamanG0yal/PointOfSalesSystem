# Point Of Sales System

This documentation outlines the models for a point of sales system, including **InventoryItem**, **Customer**, **Staff**, and **Transaction** models. Each section covers field descriptions, relationships, and example usage for interacting with the system.

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






```


# Customer Model Documentation

This documentation outlines the details of the `Customer` model, including field descriptions, relationships, and example usage.

---

## **Model: Customer**

The `Customer` model stores information about customers, including their ID, name, email, and contact number.

### **Fields**

| Field Name  | Data Type   | Description                      | Example                |
|-------------|-------------|----------------------------------|------------------------|
| `c_ID`      | Integer     | Unique identifier for a customer.| `101`                 |
| `c_name`    | String      | Name of the customer.            | `John Doe`            |
| `c_email`   | String      | Email address of the customer.   | `johndoe@example.com` |
| `c_contact` | String      | Contact number of the customer.  | `+1234567890`         |

### **Relationships**

- **No direct relationships defined** for this model in this example. If this model links to others, relationships should be defined explicitly (e.g., `Orders` or `Invoices`).

---

## **Example Usage**

### **Creating a Customer**
```python
# Example: Creating a new customer instance
customer = Customer(
    c_ID=101,
    c_name="John Doe",
    c_email="johndoe@example.com",
    c_contact="+1234567890"
)
customer.save()
# Example: Fetching a customer by ID
customer = Customer.objects.get(c_ID=101)
print(customer.c_name)  # Output: John Doe
# Example: Updating the customer's contact number
customer = Customer.objects.get(c_ID=101)
customer.c_contact = "+0987654321"
customer.save()
# Example: Deleting a customer record
customer = Customer.objects.get(c_ID=101)
customer.delete()
