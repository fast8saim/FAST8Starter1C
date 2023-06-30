# fast8_main.py

import fast8_file_system
import fast8_engine_v8
import fast8_interface

bases_list = fast8_engine_v8.parse_ibases(fast8_file_system.get_ibases_content())
fast8_interface.create_main_window(bases_list)
