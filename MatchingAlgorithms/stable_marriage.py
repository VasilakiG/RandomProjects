import random


def stable_marriage(mentors, mentees):
    #Initialize free mentors and mentees
    free_mentors = list(mentors.keys())
    free_mentees = list(mentees.keys())

    #Intialize the matching
    mentor_assignments = {}
    mentee_assignments = {}

    #Helper function to check if a mentee prefers a mentor over another mentor
    def prefers_new_mentor(mentee, new_mentor, current_mentor):
        if mentee not in mentee_assignments:
            return True
        return mentees[mentee].index(new_mentor) < mentees[mentee].index(current_mentor)

    
    #Matching process
    while free_mentors:
        mentor = free_mentors[0]
        mentor_preferences = mentors[mentor]

        #Iterate through mentors preferences
        for mentee in mentor_preferences:
            if mentee in free_mentees:
                mentor_assignments[mentor] = mentee
                mentee_assignments[mentee] = mentor
                free_mentors.remove(mentor)
                free_mentees.remove(mentee)
                break
            else:
                current_mentor = mentee_assignments[mentee]
                if prefers_new_mentor(mentee, mentor, current_mentor):
                    mentor_assignments[mentor] = mentee
                    mentee_assignments[mentee] = mentor
                    free_mentors.remove(mentor)
                    # Add the current mentor back to the free mentors list
                    free_mentors.append(current_mentor)
                    break

    return mentor_assignments


mentors = {
    'Nadica': random.sample(['Rade', 'Matej', 'Tomi', 'Vasilaki', 'Viktor', 'Stefan', 'Miro', 'Kamelija', 'Sterjev', 'Daniel', 'Ivana', 'Kaja'], 12),
    'Mrce': random.sample(['Stefan', 'Rade', 'Matej', 'Tomi', 'Viktor', 'Ivana', 'Kaja', 'Miro', 'Vasilaki', 'Sterjev', 'Daniel', 'Kamelija'], 12),
    'Gjo': random.sample(['Daniel', 'Viktor', 'Stefan', 'Rade', 'Tomi', 'Miro', 'Matej', 'Vasilaki', 'Ivana', 'Sterjev', 'Kamelija', 'Kaja'],12),
    'Nikola': random.sample(['Viktor', 'Kamelija', 'Tomi', 'Vasilaki', 'Sterjev', 'Miro', 'Rade', 'Ivana', 'Matej', 'Daniel', 'Stefan', 'Kaja'], 12),
    'Eva': random.sample(['Kamelija', 'Stefan', 'Rade', 'Tomi', 'Vasilaki', 'Miro', 'Matej', 'Ivana', 'Daniel', 'Kaja', 'Sterjev', 'Viktor'], 12),
    'Krango': random.sample(['Kaja', 'Kamelija', 'Miro', 'Vasilaki', 'Rade', 'Ivana', 'Matej', 'Tomi', 'Sterjev', 'Daniel', 'Viktor', 'Stefan'], 12),
    'Nina': random.sample(['Kaja', 'Tomi', 'Viktor', 'Ivana', 'Sterjev', 'Stefan', 'Miro', 'Rade', 'Matej', 'Vasilaki', 'Kamelija', 'Daniel'], 12),
    'Dadi': random.sample(['Tomi', 'Miro', 'Rade', 'Vasilaki', 'Kaja', 'Daniel', 'Ivana', 'Sterjev', 'Matej', 'Kamelija', 'Viktor', 'Stefan'], 12),
    'Pepo': random.sample(['Miro', 'Kaja', 'Tomi', 'Rade', 'Vasilaki', 'Matej', 'Kamelija', 'Ivana', 'Daniel', 'Sterjev', 'Stefan', 'Viktor'], 12),
    'Maneva': random.sample(['Sterjev', 'Miro', 'Rade', 'Tomi', 'Kamelija', 'Kaja', 'Vasilaki', 'Ivana', 'Daniel', 'Stefan', 'Matej', 'Viktor'], 12),
    'Bazho': random.sample(['Tomi', 'Miro', 'Rade', 'Vasilaki', 'Daniel', 'Ivana', 'Sterjev', 'Matej', 'Kamelija', 'Kaja', 'Stefan', 'Viktor'], 12),
    'Slavejkov': random.sample(['Vasilaki', 'Kamelija', 'Tomi', 'Rade', 'Miro', 'Matej', 'Kaja', 'Ivana', 'Sterjev', 'Daniel', 'Stefan', 'Viktor'], 12)
}


mentees = {
    'Vasilaki': random.sample(['Nadica', 'Mrce', 'Gjo', 'Nikola', 'Eva', 'Krango', 'Nina', 'Dadi', 'Pepo', 'Maneva', 'Bazho', 'Slavejkov'], 12),
    'Daniel': random.sample(['Mrce', 'Nadica', 'Gjo', 'Nikola', 'Eva', 'Krango', 'Nina', 'Dadi', 'Pepo', 'Maneva', 'Bazho', 'Slavejkov'], 12),
    'Rade': random.sample(['Nadica', 'Gjo', 'Mrce', 'Nikola', 'Eva', 'Krango', 'Nina', 'Dadi', 'Pepo', 'Maneva', 'Bazho', 'Slavejkov'], 12),
    'Matej': random.sample(['Gjo', 'Mrce', 'Nadica', 'Nikola', 'Eva', 'Krango', 'Nina', 'Dadi', 'Pepo', 'Maneva', 'Bazho', 'Slavejkov'], 12),
    'Viktor': random.sample(['Nikola', 'Mrce', 'Gjo', 'Nadica', 'Eva', 'Krango', 'Nina', 'Dadi', 'Pepo', 'Maneva', 'Bazho', 'Slavejkov'], 12),
    'Kaja': random.sample(['Gjo', 'Nina', 'Krango', 'Nadica', 'Eva', 'Mrce', 'Nikola', 'Dadi', 'Pepo', 'Maneva', 'Bazho', 'Slavejkov'], 12),
    'Kamelija': random.sample(['Krango', 'Gjo', 'Nina', 'Nadica', 'Eva', 'Mrce', 'Nikola', 'Dadi', 'Pepo', 'Maneva', 'Bazho', 'Slavejkov'], 12),
    'Tomi': random.sample(['Gjo', 'Mrce', 'Nadica', 'Nikola', 'Eva', 'Krango', 'Nina', 'Dadi', 'Pepo', 'Maneva', 'Bazho', 'Slavejkov'], 12),
    'Stefan': random.sample(['Gjo', 'Mrce', 'Nadica', 'Eva', 'Krango', 'Nina', 'Nikola', 'Dadi', 'Pepo', 'Maneva', 'Bazho', 'Slavejkov'], 12),
    'Ivana': random.sample(['Gjo', 'Mrce', 'Nadica', 'Eva', 'Krango', 'Nina', 'Nikola', 'Dadi', 'Pepo', 'Maneva', 'Bazho', 'Slavejkov'], 12),
    'Miro': random.sample(['Krango', 'Gjo', 'Nina', 'Nadica', 'Eva', 'Mrce', 'Nikola', 'Dadi', 'Pepo', 'Maneva', 'Bazho', 'Slavejkov'], 12),
    'Sterjev': random.sample(['Gjo', 'Nina', 'Krango', 'Nadica', 'Eva', 'Mrce', 'Nikola', 'Dadi', 'Pepo', 'Maneva', 'Bazho', 'Slavejkov'], 12)
}

matches = stable_marriage(mentors, mentees)

for mentor, mentee in matches.items():
    print(f"{mentor} is matched with {mentee}")
