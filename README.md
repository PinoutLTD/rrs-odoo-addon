## Robnomics Report Service: Addon for Odoo

Odoo addon to store information about Robonomics Report Service users. 

---

Requirements:

1. [Odoo Community version 16.0](https://www.odoo.com/documentation/16.0/administration/install/source.html)
2. [Odoo Outgoing Webhooks addon](https://apps.odoo.com/apps/modules/16.0/base_automation_webhook/)
3. [Odoo Invoicing addon](https://www.odoo.com/app/invoicing)

---

Instalaltion:

```
mkdir ~/src/custom
cd ~/src/custom
git clone https://github.com/PinoutLTD/rrs-odoo-addon.git
```

Post installation:

A `Robonomics Subscription` product should be created. Navigate to Invoicing -> Products and create a new Product with the name `Robonomics Subscription 1 month`

`paid` and `not paid` statuses should be created on Robonomics Report Service addon. Navigate to Robonomics Report Service -> Dashboard -> Status and create `paid` and `not paid` statuses.

To ensure the proper functioning of the Robonomics Report Service, it's necessary to set up specific Automated Actions. In Odoo, navigate to Settings -> Technical -> Automation -> Automated Actions.

1. Create an action with the name `invoice email`. Model: `Journal Entry`, Trigger `On Update`, Trigger Fields `Status (account.move)`, Apply on: `[("invoice_line_ids.product_id", "=", "Robonomics Subscription 1 month")]`, Action To Do: `Send Email`, Email Template: `Invoice: Sending`, Send as `Email`.

2. Create an action with the name `rrs_payment`. Model: `Robonomics Report Service Register`, Trigger `On Update`, Trigger Fields `Status (rrs.register)`, Action To Do: `Execute Python Code`. Add the following code to the `Python Code` field, specifying the correct address of your [RRS Registar](https://github.com/PinoutLTD/rrs-registrar.git).

```
WEBHOOK=,your RRS Registar address.
data = {
    "id": record.id,
    "email": record.customer_email,
    "address": record.address,
    "status": record.status.id,
    "owner_address": record.owner_address
}
make_request("POST", WEBHOOK, json=data)
```

Launch:

Launch Odoo providing the addon's path:

```
python3 odoo-bin --addons-path=addons,../src/custom/helpdesk,../src/custom/rrs-odoo-addon --workers 2
```