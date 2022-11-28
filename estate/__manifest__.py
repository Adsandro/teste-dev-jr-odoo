{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Adsandro Carvalho",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
            #DEVE SER IMPLEMENTADO TODAS AS APLICAÇÕES CRIADAS, INFORMANDO O NOME DA PASTA E O ARQUIVO
           'security/ir.model.access.csv',
            'views/estate_property_views.xml',
            'views/estate_menus.xml',
                
    ],
    # data files containing optionally loaded demonstration data
    'demo': [



    ],
    
    'application': True,
}