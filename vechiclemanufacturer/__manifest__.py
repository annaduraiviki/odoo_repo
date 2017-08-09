{
'name': "Vehicle management system",
'summary': "Vehicle manufacturing system management system",
'description':""" Vehicle manufacturing system management system. Maintain Vechicle service with custom. Development stage""",
'author': "VA",
'website': "viki2.odoo.com",
'category': 'custom',
'version':'10.c',
'depends':['base','sale','mail','customcountrystate','board'],
'data':[
     'views/production.xml',
     'views/carparts.xml',
     'views/service.xml',
    'security/vechicle_security.xml',
    'security/ir.model.access.csv',
      'views/login.xml',
     'wizard/customer_wizard_xml.xml',
     'wizard/customer_wizard_xml2.xml',
      'views/customer.xml',
    'views/companymanagement.xml',
      'views/supplier.xml',
      'views/serviceman.xml',
      #'views/report_customer.xml',
      #'customer_report.xml',
     #'views/partner.xml',
      'views/partsprovider_view.xml',
       'views/companyleavemanagement_view.xml',
      'views/token_reservation_view.xml',
      'views/products_view.xml',
      'views/products_menu.xml',
       #'views/view_window.xml',
      # 'views/javascript_sample.xml',
     #'views/customerpipeline_view.xml',
      'views/quotation-pipeline.xml',
      'views/report_supplier.xml',
      'supplier_report.xml',
      'views/dashboard_vechicle.xml',


        ],


# Remove this div button part, when newly installed ths app in customer.xml. add after install
#                             <div
#                         class="oe_button_box oe_subtotal_footer_separator oe_inline o_td_label"
#                         name="button_box">
#                         <button name="%(vechiclemanufacturer.supplier_action_window)d"
#                             type="action" class=" oe_right o_wow oe_stat_button" icon="fa-inr"
#                             context="{'search_default_cust_id': active_id}">
#                             <field name="customer_tot_cost" widget="statinfo"></field>
#                         </button>
#                         <button name="_priority_but" type="action" class="oe_right oe_stat_button"
#                             icon="fa-bolt">
#                             <field name="priority_but" widget='statinfo' />
#                         </button>
#                     </div>


}
