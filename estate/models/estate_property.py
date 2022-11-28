from odoo import fields, models
from dateutil.relativedelta import relativedelta


#Define função para retornar a data de disponibilidade em 3 meses, ela é utilizada em date_availability




class EstateProperty(models.Model):

    def _default_date_availability(self):
        return fields.Date.context_today(self) + relativedelta(months=3)

    _name = "estate.property"
    _description = "test Model"
    postcode = fields.Char("Postcode")
    date_availability = fields.Date("Available From", default=lambda self: self._default_date_availability(), copy=False) #Não é possivel ser copiado
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", copy=False, readonly=True) #Define para apenas leitura
    bedrooms = fields.Integer("Bedrooms", default=2) #Define que o numero parão de quartos é igual a 2
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area (sqm)")
    garden_orientation = fields.Selection(
        selection=[

                    ("N", "North"),
                    ("S", "South"),
                    ("E", "East"),
                    ("W", "West"),           
                                    ],
                    string="Garden Orientation",)

    active = fields.Boolean("Active", default=True)


    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
    )