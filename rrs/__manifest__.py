{
    "name": "Robonomics Report Service",
    "version": "16.0",
    "application": True,
    "depends": ["base"],
    "data": [
        "security/rss_security.xml",
        "security/ir.model.access.csv",
        "views/rrs_register_status.xml",
        "views/rrs_register.xml",
        "views/menu.xml"
    ],
    "installable": True,
    'license': 'LGPL-3',
}