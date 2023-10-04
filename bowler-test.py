from bowler import Bowler

def main():
    # Nasir famous as nas is a right arm bowler played several matches
    nasir_pak = Bowler("Nas", "right")
    nasir_pak.Match = "India", 232, 4
    nasir_pak.Match = "India", 187, 2
    nasir_pak.Match = "England", 182, 5
    nasir_pak.Match = "Kenya", 102, 3
    nasir_pak.Match = "India", 78, 1
    nasir_pak.Match = "Australia", 260, 3
    nasir_pak.Match = "Australia", 170, 5
    nasir_pak.Match = "India", 127, 7

    # record of Nasir saved is
    print(str(nasir_pak))
    print("Five wickets matches count:", str(nasir_pak.fiveWichets))

    nasir_pak.updateWickets(2, 6)    
    nasir_pak.update(6, ("zimbabwe", 260, 3))
    nasir_pak.update(7, ("zimbabwe", 140, 4))
    nasir_pak.updateWickets(8, 4)    
    
    # updated record of Nasir saved is
    print("\nUpdated record ******")
    print(str(nasir_pak))
    print("Five wickets matches count:", str(nasir_pak.fiveWichets))

    # Match 5
    print("\nMatch 5 is ******")
    # print(str(nasir_pak.Match(5)))
    print(str(nasir_pak.Match))


if __name__ == "__main__":
    main()
