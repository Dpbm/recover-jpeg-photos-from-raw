import sys
import os


def main(image_raw_input_file):

    with open(image_raw_input_file, 'rb') as archive:

        image_amount_counter = 0
        found_an_image = False
        readied_bytes = 0
        file_len = os.path.getsize(image_raw_input_file)
        new_image_file = None


        while readied_bytes != file_len:
            buffer = archive.read(512)
            readied_bytes += 512


            if (hex(buffer[0]) == '0xff' and 
            hex(buffer[1]) == '0xd8' and 
            hex(buffer[2]) == '0xff' and 
            hex(buffer[3] & 0xf0) == '0xe0'):
                if (found_an_image):
                    new_image_file.close()
                    image_amount_counter += 1

                new_image_file = open(f'./{image_amount_counter}.jpeg', 'wb')
                found_an_image = True
            
                        
            if(found_an_image):
                new_image_file.write(buffer)
                

if __name__ == '__main__':
    
    argv = sys.argv

    if(len(argv) != 2):
        print('Usage: python image')
        exit(1)

    if(not argv[-1]):
        print('Usage: python image')
        exit(1)

    image_raw_input_file = argv[-1]

    main(image_raw_input_file)