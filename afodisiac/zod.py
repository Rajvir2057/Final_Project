


def get_zodiac_signs(month, day):
    zodiac_signs = {
    "Aries": "unafraid of conflict, highly competitive, and honest",
    "Taurus": "Sensual,emotionally strong and hardworking,",
    "Gemini": "curious, clever, and outstanding communicators who are pretty unpredictable",
    "Cancer": "Nurturing and loyal",
    "Leo": "Generous, warmhearted, creative, enthusiastic, and faithful.",
    "Virgo": "diligent workers who excel at what they do, but their lofty ambitions can lead them to be too critical of others.",
    "Libra": "extroverted, cosy, and friendly people",
    "Scorpio": "strong, enigmatic and independent characters who crackle with an intensity and charisma that makes them un-ignorable.",
    "Sagittarius": "adventurers, risk-takers, and have a sharp business and sports mentality.",
    "Capricorn": "perfectionist, hardworking, and organised.",
    "Aquarius": " intellectual, thoughtful, charismatic, and an expert communicator.",
    "PIsces": "imaginative, creative, kind, supportive, people-smart, emotional intelligent, intuitive (even psychic), and able to see beyond the façade to the truth of things."
}
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries", zodiac_signs['Aries']
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus", zodiac_signs['Taurus']
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini", zodiac_signs['Gemini']
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer", zodiac_signs['Cancer']
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo", zodiac_signs['Leo']
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo", zodiac_signs['Virgo']
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra", zodiac_signs['Libra']
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio", zodiac_signs['Scorpio']
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius", zodiac_signs['Sadittarius']
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn", zodiac_signs['Capricorn']
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius", zodiac_signs['Aquarius']
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces", zodiac_signs['Pisces']
    else:
        return "Invalid input", ""


def main():
    month = int(input("Enter your birth month (as a number): "))
    day = int(input("Enter your birth day (as a number): "))

    sign, characteristics = get_zodiac_signs(month, day)
    if sign != "Invalid input":
        print("Your zodiac sign is:", sign)
        print("Characteristics of", sign, ":", characteristics)
    else:
        print("Invalid input. Please enter a valid month and day.")



if __name__ == "__main__":
    main()