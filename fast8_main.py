# fast8_main.py

import fast8_form_create
import fast8_file_system
import fast8_engine_v8

bases_list = fast8_engine_v8.parse_ibases(fast8_file_system.get_ibases_content())
fast8_form_create.create_main_form(bases_list)