





def main():
    done = False
    while not done:
        try:
            file = raw_input("Enter the filename of the image you'd like to use:")
            
            x = raw_input"What would you like to do with this file?"
            if x = "Scrolling":
                Scrolling(file)
                canvas.display()
            done = True
        except:
            print("That is not an available filename.")
            done = False
main()