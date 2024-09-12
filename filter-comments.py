import os
import xml.etree.ElementTree as ET

import xml.etree.ElementTree as ET

def filter_comments(file_path, output_file):
    # Parse the XML file into an ElementTree object
    tree = ET.parse(file_path)
    root = tree.getroot()
    keep_list = ['julie.jones@pobox.com',
        'daniel.hardman@gmail.com',
        'steve.tolman@gmail.com',
        'don_kleinschnitz@hotmail.com',
        'kim@kd7ike.info',
        'norsk5@yahoo.com',
        'rrkillian@rktoyandhobby.com',
        'elforesto@gmail.com',
        'stanleysawyer684@yahoo.com',
        'jasonivey@gmail.com',
        'stas.shaposhnikov@gmail.com',
        'drjaz@hotmail.com',
        'jesse@coolestfamilyever.com',
        'jasonivet@gmail.com',
        'andy3474@msn.com',
        'trevharmon@gmail.com',
        'dennes777@gmail.com',
        'ryancorradini@yahoo.com',
        'mike_ebert@twitter.example.com',
        'david@handysoftware.com',
        'const.nekrasoff@gmail.com',
        'bsaville@adaptivecomputing.com',
        'nwwells@gmail.com',
        'j.henry@n-dexed.com',
        'Enthouan@twitter.example.com',
        'tuga2112@hotmail.com',
        'dhaffey@gmail.com',
        'mraffel@ugenius.com',
        'sswinsick@gmail.com',
        'briansbellon@gmail.com',
        'daedtech@twitter.example.com',
        'lovelymutti@gmail.com',
        'carl@appellof.org',
        'shawn.holmstead@gmail.com',
        'bwistisen@gmail.com',
        'iannate@gmail.com',
        'lisaan@juno.com',
        'herb.sutter@gmail.com',
        'sandford@jhu.edu',
        'coleb@eyesopen.com',
        'rananthu@outlook.com',
        'spam@earwicker.com',
        'rob@stutton.net',
        'genehughson@hotmail.com',
        'rickmckay@gmail.com',
        'anthony.langsworth@gmail.com',
        'ardanew@mail.ru',
        'jason@lawcasa.com',
        'mbelnap@adaptivecomputing.com',
        'middlefraz@yahoo.com',
        'eprusse@comcast.net',
        'francois.reynald@bettersoftwareprojects.com',
        'ralfmc@gmail.com',
        'tian.tian098@gmail.com',
        'pmhut2@itoctopus.com',
        'ryan@rmarcus.info',
        'weberc2@gmail.com',
        'bradykimball@twitter.example.com',
        'kc5tja@arrl.net',
        'kun.jeremy@gmail.com',
        'vladimir.starostenkov@gmail.com',
        'stereomatchingkiss@gmail.com',
        'j@razemail.com',
        'quicknir@gmail.com',
        'bastian.erdnuess@gmail.com',
        'whatsbottle@outlook.com',
        'n_botm@hotmail.com',
        'lkafle@gmail.com',
        'you.neednt@my.mail',
        'balelinits@gmail.com',
        'djkaty@start.no',
        'lol@internet.co.uk',
        'codecraft.co.ns4u@jeterworld.net',
        'krmane@openmailbox.org',
        'dennis.stritzke@googlemail.com',
        'dave@daverea.com',
        'laurent.caillette@gmail.com',
        'cormacc@gmail.com',
        'mattias.eppler@groz-beckert.com',
        'zebal@protonmail.ch',
        'dmaclach@gmail.com',
        'f.grossweiner@gmail.com',
        'rune@paamand.eu',
        'craig@craiglaurence.com',
        'steve@crocker.com',
        'mbking42@aol.com',
        'wordpress@earwicker.com',
        'moberlin05@gmail.com',
        'sean_moe@byu.edu',
        'lannistertyrion231@gmail.com',
        'codecraft@utahlan.com',
        'tricky1@sms.at',
        'shoebtanjim@gmail.com']
    drop_list = ['maddyb12@aim.com',
        'ronnieworsham@yahoo.de',
        'agueda.gregory@arcor.de',
        'kerrymcclung@arcor.de',
        'penney_covert@inbox.com',
        '14mnkq+9vsjgu0t6v01k@sharklasers.com',
        'virgilellsworth@googlemail.com',
        'petramoffett@googlemail.com',
        'carmon.grenier@web.de',
        'cassie.fierro@googlemail.com',
        'charityomalley@fmail.co.uk',
        'madison.ness@fastmailbox.net',
        'beth@segmation.com',
        'corinnewall798@yahoo.com',
        'andrewtitenko378@yahoo.com',
        'sparksofmelody460@gmail.com']
    namespaces = {'wp': 'http://wordpress.org/export/1.2/'}
    for channel in root.findall(".//channel", namespaces):
        # Loop through the children of <channel> to track the parent of each <wp:comment>
        comments_to_remove = []
        for comment in channel.findall("wp:comment", namespaces):
            # Find the <wp:comment_author_email> child tag
            author_email = comment.find("wp:comment_author_email", namespaces)
            
            if author_email is not None and author_email.text is not None:
                email = author_email.text
                if email in keep_list:
                    continue
                if email in drop_list:
                    comments_to_remove.append(comment)
                    continue
                # Display the email content and prompt the user
                print(f"Author email: {author_email.text}")
                user_input = input("Keep this comment? (Yes/no): ").strip().lower()
                # If the user says "no", remove the <wp:comment> element
                if user_input.startswith('n'):
                    drop_list.append(email)
                    comments_to_remove.append(comment)
                else:
                    keep_list.append(email)
        for comment in comments_to_remove:
            channel.remove(comment) 
        comments_to_remove = []

    # Save the modified tree to the output file
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

# Example usage
input_file = 'data.xml'
output_file = 'filtered.xml'

filter_comments(input_file, output_file)

