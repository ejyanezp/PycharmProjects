import re
import logging
from logging.handlers import RotatingFileHandler


def process_java_service_file(name: str, p_logger: logging.Logger):
    # Load Java Code
    input_java_file = open(name, 'r')
    java_code = [text_line for text_line in input_java_file]
    input_java_file.close()
    output_code = []
    # Look for a static class declaration, get the class name
    reg_express = "\\s*public\\s+static\\s+class\\s+([A-Z][A-za-z]+)\\s+{\\s*"
    state = 0
    p_logger.info('Status 0')
    for line in java_code:
        matches = re.findall(reg_express, line)
        blank_count = len(line) - len(line.lstrip())
        spc = " " * blank_count
        if state == 0:
            if len(matches) > 0:
                class_name = matches[0]
                output_code.append(f"{spc}@ApiModel(description=\"{class_name}\")")
                # Now look for fields declarations, get the type and field names
                # Will get a list of tuples (Type, variable name)
                reg_express = "\\s*([\\/\\/\\s*A-Za-z]+)\\s+([a-zA-z]+);"
                state = 1
                p_logger.info('Status 1')
        elif state == 1:
            if len(matches) > 0:
                # If the next line is commented out, do not put the annotation.
                if not matches[0][0].startswith("//"):
                    field_name = matches[0][1]
                    output_code.append(f"{spc}@ApiModelProperty(value=\"{field_name}\")")
            elif line.strip() == '}':
                state = 2
                p_logger.info('Status 2')
        output_code.append(line.rstrip())
    # Print the result (put "++" to distinguish the output from the original file).
    for line in output_code:
        print(f"++{line}")


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]: %(message)s',
                    level=logging.DEBUG,
                    filename='parser.log')
# implement rotating logs
logger = logging.getLogger('test_logger')
handler = RotatingFileHandler('parser.log', maxBytes=20*1024*1024, backupCount=5)
logger.info('Started')
process_java_service_file('CRUDOLAPIsService.java', logger)
logger.info('Finished')
