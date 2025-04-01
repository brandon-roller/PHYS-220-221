

if __name__ == "__main__":
    with open("lock-in_output.txt", "r") as read:
        with open("output_sanitized.txt", "w") as write:
            lines = read.readlines()
            for line in lines:
                for num in line.split(" "):
                    write.write(f"{float(num):.6f}\t")
                write.write("\n")
