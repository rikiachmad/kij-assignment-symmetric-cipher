from app import App
import sys
import logging

def main():
    logging.basicConfig(level=logging.DEBUG)
    app = App()
    arg_len = len(sys.argv)
    command = sys.argv[1]

    if command == "send":
        if arg_len < 4:
            logging.exception(f"Not enough arguments for send command. Expected: 2 got {arg_len - 2}")
            return
        try:
            filename = sys.argv[2]
            cipher = sys.argv[3]
            logging.info("sending file..")
            app.send_file(filename, cipher)
        except Exception as e:
            logging.exception(e)
            return

        logging.info("file sent successfully!")

    elif command == "receive":
        while True:
            try:
                app.receive_file()
            except Exception as e:
                logging.exception(e)
                return
            logging.info("file received succesfully!")
    
    else:
        logging.exception(f"Command not found for {command}")
        return


if __name__ == "__main__":
    main()