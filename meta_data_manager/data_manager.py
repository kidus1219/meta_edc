from edc_data_manager.site_data_manager import site_data_manager

from .handlers import BaselineHbA1cRuleHandler

site_data_manager.register(BaselineHbA1cRuleHandler)
