---
name: place_order
description: Complete customer order workflow
type: workflow
triggers:
  - intent: "我想下单"
  - intent: "创建订单"
---

# Place Order Workflow

When the user expresses intent to place an order, execute the following steps:

## Step 1: Validate Payment
Call `validate_payment` action with the provided payment information.
If validation fails, abort the workflow and return an error.

## Step 2: Check Inventory
Call `check_inventory` action with product_id and quantity.
If inventory is insufficient, abort and notify user.

## Step 3: Create Order
Call `create_order` action with customer_id, product_id, quantity.
Save the returned order_id.

## Step 4: Send Notification
Call `send_notification` action with order details.
