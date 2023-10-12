from flask import Flask, request, render_template
import json
import sys




total_capture = 0
def localhost(password, port, jsonfile, loginfile, inboxfile, host="127.0.0.1"):
    app = Flask("sms_forwarder")
    set_password = password
    @app.route('/', methods=['GET', 'POST'])
    def index():
        global total_capture
        if (request.method == 'POST'):
            password = request.form['password']
            if (password == set_password):
                while True:
                    log_events = json.loads(open(jsonfile, "r").read())
                    len_data = len(log_events)
                    if total_capture > 99:
                        total_capture = 0
                        with open(jsonfile, "w") as file:
                            file.write("[]")
                        Inner_html = '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=1024, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
        <title>Sms Forwarder - Inbox</title>
        <style>
            /* Reset some default styles */
            body, ul {
                margin: 0;
                padding: 0;
                list-style: none;
            }

            /* Global styles */
            body {
                font-family: Arial, sans-serif;
            }

            /* Header styles */
            header {
                background-color: #2d89ef;
                color: white;
                padding: 20px;
                text-align: center;
            }

            h1 {
                margin: 0;
                font-size: 24px;
            }

            /* Navigation styles */
            nav ul {
                background-color: #f0f0f0;
                text-align: center;
                padding: 10px;
            }

            nav li {
                display: inline;
                margin: 0 10px;
            }

            nav .reload-button {
                display: inline-block;
                background-color: #5e6e17fb;
                color: white;
                padding: 10px 100px;
                border-radius: 5px;
                text-decoration: none;
                cursor: pointer;
            }

            /* Email list styles */
            .email-list {
                padding: 20px;
            }

            .email-item {
                background-color: #fff;
                border: 1px solid #ddd;
                margin: 10px 0;
                padding: 15px;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                cursor: pointer;
                transition: background-color 0.3s, transform 0.3s;
            }

            .email-item:hover {
                background-color: #f5f5f5;
                transform: translateY(-2px);
            }

            .email-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 10px;
            }

            .sender {
                font-weight: bold;
            }

            .subject {
                flex-grow: 1;
                margin-left: 20px;
                overflow: hidden;
                white-space: nowrap;
                text-overflow: ellipsis;
            }

            .date {
                font-size: 12px;
                color: #888;
            }

            .email-details {
                display: none;
                background-color: #f0f0f0;
                border: 1px solid #ddd;
                padding: 10px;
                margin-top: 10px;
                border-radius: 5px;
            }

            .email-item.expanded .email-details {
                display: block;
            }

            a {
                text-decoration: none;
                color: #2d89ef;
                font-weight: bold;
            }
            /* Define the animation */
            @keyframes pulse {
            0% {
                transform: scale(1);
            }
            50% {
                transform: scale(0.5);
            }
            100% {
                transform: scale(0.1);
            }
            }

            /* Apply the animation class */
            .animate {
            animation: pulse 1s infinite;
            }
        </style>
    </head>
    <body>
        <header>
            <h1 style="font-family: algerian; font-size: 50px; color: black;">SMS FORWARDER</h1>
        </header>
        <nav>
            <ul>
                <li>
                    <a href="#" class="reload-button" id="reloadInbox">Refresh</a>
                </li>
            </ul>
        </nav>
        <main>
            <ul>
                <!-- hgcs_1 -->
                <!-- hgcs_2 -->
                <!-- hgcs_3 -->
                <!-- hgcs_4 -->
                <!-- hgcs_5 -->
                <!-- hgcs_6 -->
                <!-- hgcs_7 -->
                <!-- hgcs_8 -->
                <!-- hgcs_9 -->
                <!-- hgcs_10 -->
                <!-- hgcs_11 -->
                <!-- hgcs_12 -->
                <!-- hgcs_13 -->
                <!-- hgcs_14 -->
                <!-- hgcs_15 -->
                <!-- hgcs_16 -->
                <!-- hgcs_17 -->
                <!-- hgcs_18 -->
                <!-- hgcs_19 -->
                <!-- hgcs_20 -->
                <!-- hgcs_21 -->
                <!-- hgcs_22 -->
                <!-- hgcs_23 -->
                <!-- hgcs_24 -->
                <!-- hgcs_25 -->
                <!-- hgcs_26 -->
                <!-- hgcs_27 -->
                <!-- hgcs_28 -->
                <!-- hgcs_29 -->
                <!-- hgcs_30 -->
                <!-- hgcs_31 -->
                <!-- hgcs_32 -->
                <!-- hgcs_33 -->
                <!-- hgcs_34 -->
                <!-- hgcs_35 -->
                <!-- hgcs_36 -->
                <!-- hgcs_37 -->
                <!-- hgcs_38 -->
                <!-- hgcs_39 -->
                <!-- hgcs_40 -->
                <!-- hgcs_41 -->
                <!-- hgcs_42 -->
                <!-- hgcs_43 -->
                <!-- hgcs_44 -->
                <!-- hgcs_45 -->
                <!-- hgcs_46 -->
                <!-- hgcs_47 -->
                <!-- hgcs_48 -->
                <!-- hgcs_49 -->
                <!-- hgcs_50 -->
                <!-- hgcs_51 -->
                <!-- hgcs_52 -->
                <!-- hgcs_53 -->
                <!-- hgcs_54 -->
                <!-- hgcs_55 -->
                <!-- hgcs_56 -->
                <!-- hgcs_57 -->
                <!-- hgcs_58 -->
                <!-- hgcs_59 -->
                <!-- hgcs_60 -->
                <!-- hgcs_61 -->
                <!-- hgcs_62 -->
                <!-- hgcs_63 -->
                <!-- hgcs_64 -->
                <!-- hgcs_65 -->
                <!-- hgcs_66 -->
                <!-- hgcs_67 -->
                <!-- hgcs_68 -->
                <!-- hgcs_69 -->
                <!-- hgcs_70 -->
                <!-- hgcs_71 -->
                <!-- hgcs_72 -->
                <!-- hgcs_73 -->
                <!-- hgcs_74 -->
                <!-- hgcs_75 -->
                <!-- hgcs_76 -->
                <!-- hgcs_77 -->
                <!-- hgcs_78 -->
                <!-- hgcs_79 -->
                <!-- hgcs_80 -->
                <!-- hgcs_81 -->
                <!-- hgcs_82 -->
                <!-- hgcs_83 -->
                <!-- hgcs_84 -->
                <!-- hgcs_85 -->
                <!-- hgcs_86 -->
                <!-- hgcs_87 -->
                <!-- hgcs_88 -->
                <!-- hgcs_89 -->
                <!-- hgcs_90 -->
                <!-- hgcs_91 -->
                <!-- hgcs_92 -->
                <!-- hgcs_93 -->
                <!-- hgcs_94 -->
                <!-- hgcs_95 -->
                <!-- hgcs_96 -->
                <!-- hgcs_97 -->
                <!-- hgcs_98 -->
                <!-- hgcs_99 -->
                <!-- hgcs_100 -->
            </ul>
        </main>
        <script>
            // JavaScript to toggle email details visibility
            const emailItems = document.querySelectorAll('.email-item');
            
            emailItems.forEach(emailItem => {
                emailItem.addEventListener('click', () => {
                    emailItem.classList.toggle('expanded');
                });
            });
        
            // JavaScript to reload the inbox
            const reloadButton = document.getElementById('reloadInbox');
            reloadButton.addEventListener('click', () => {
                reloadButton.classList.add('animate');
                setTimeout(function() {
                    reloadButton.classList.remove('animate');
                }, 1000);
                location.reload();
            });
        
            // JavaScript to reload the inbox every 10 seconds
            const reloadEvery7Seconds = () => {
                location.reload();
            };
        
            // Call the reload function initially and then every 10 seconds
            setTimeout(reloadEvery7Seconds, 7000); // Call it initially
        </script>
        
    </body>
    </html>
    '''
                        with open(f"templates/{inboxfile}", "w") as file:
                                    file.write(Inner_html)
                    if (len_data != total_capture):
                            try:
                                unsended_info  = int(str(len_data - total_capture).replace("-", ""))
                                unsend_message = log_events[-unsended_info:]
                                for unsended_count in range(unsended_info):
                                    total_capture += 1

                                    name = unsend_message[unsended_count].get("sender")
                                    number = unsend_message[unsended_count].get("number")
                                    date = unsend_message[unsended_count].get("date")
                                    message = unsend_message[unsended_count].get("message")

                                    Html = open(f"templates/{inboxfile}").read()
                                    Items = f'''
                    <li class="email-item">
                        <div class="email-header">
                            <span class="sender">{name}</span>
                            <span class="subject">{number}</span>
                            <span class="date">{date}</span>
                        </div>
                        <div class="email-details">
                            <p>{message}</p>
                        </div>
                    </li>'''

                                    with open(f"templates/{inboxfile}", "w") as file:
                                        file.write(Html.replace(f"<!-- hgcs_{total_capture} -->", Items))
                            except IndexError: pass
                    else:
                        return render_template(inboxfile)
            else: return render_template(loginfile)
        return render_template(loginfile)
    app.run(debug=True, host=host, port=port)
    
    with open(jsonfile, "w") as file:
        file.write("[]")
    Inner_html = '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=1024, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
        <title>Sms Forwarder - Inbox</title>
        <style>
            /* Reset some default styles */
            body, ul {
                margin: 0;
                padding: 0;
                list-style: none;
            }

            /* Global styles */
            body {
                font-family: Arial, sans-serif;
            }

            /* Header styles */
            header {
                background-color: #2d89ef;
                color: white;
                padding: 20px;
                text-align: center;
            }

            h1 {
                margin: 0;
                font-size: 24px;
            }

            /* Navigation styles */
            nav ul {
                background-color: #f0f0f0;
                text-align: center;
                padding: 10px;
            }

            nav li {
                display: inline;
                margin: 0 10px;
            }

            nav .reload-button {
                display: inline-block;
                background-color: #5e6e17fb;
                color: white;
                padding: 10px 100px;
                border-radius: 5px;
                text-decoration: none;
                cursor: pointer;
            }

            /* Email list styles */
            .email-list {
                padding: 20px;
            }

            .email-item {
                background-color: #fff;
                border: 1px solid #ddd;
                margin: 10px 0;
                padding: 15px;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                cursor: pointer;
                transition: background-color 0.3s, transform 0.3s;
            }

            .email-item:hover {
                background-color: #f5f5f5;
                transform: translateY(-2px);
            }

            .email-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 10px;
            }

            .sender {
                font-weight: bold;
            }

            .subject {
                flex-grow: 1;
                margin-left: 20px;
                overflow: hidden;
                white-space: nowrap;
                text-overflow: ellipsis;
            }

            .date {
                font-size: 12px;
                color: #888;
            }

            .email-details {
                display: none;
                background-color: #f0f0f0;
                border: 1px solid #ddd;
                padding: 10px;
                margin-top: 10px;
                border-radius: 5px;
            }

            .email-item.expanded .email-details {
                display: block;
            }

            a {
                text-decoration: none;
                color: #2d89ef;
                font-weight: bold;
            }
            /* Define the animation */
            @keyframes pulse {
            0% {
                transform: scale(1);
            }
            50% {
                transform: scale(0.5);
            }
            100% {
                transform: scale(0.1);
            }
            }

            /* Apply the animation class */
            .animate {
            animation: pulse 1s infinite;
            }
        </style>
    </head>
    <body>
        <header>
            <h1 style="font-family: algerian; font-size: 50px; color: black;">SMS FORWARDER</h1>
        </header>
        <nav>
            <ul>
                <li>
                    <a href="#" class="reload-button" id="reloadInbox">Refresh</a>
                </li>
            </ul>
        </nav>
        <main>
            <ul>
                <!-- hgcs_1 -->
                <!-- hgcs_2 -->
                <!-- hgcs_3 -->
                <!-- hgcs_4 -->
                <!-- hgcs_5 -->
                <!-- hgcs_6 -->
                <!-- hgcs_7 -->
                <!-- hgcs_8 -->
                <!-- hgcs_9 -->
                <!-- hgcs_10 -->
                <!-- hgcs_11 -->
                <!-- hgcs_12 -->
                <!-- hgcs_13 -->
                <!-- hgcs_14 -->
                <!-- hgcs_15 -->
                <!-- hgcs_16 -->
                <!-- hgcs_17 -->
                <!-- hgcs_18 -->
                <!-- hgcs_19 -->
                <!-- hgcs_20 -->
                <!-- hgcs_21 -->
                <!-- hgcs_22 -->
                <!-- hgcs_23 -->
                <!-- hgcs_24 -->
                <!-- hgcs_25 -->
                <!-- hgcs_26 -->
                <!-- hgcs_27 -->
                <!-- hgcs_28 -->
                <!-- hgcs_29 -->
                <!-- hgcs_30 -->
                <!-- hgcs_31 -->
                <!-- hgcs_32 -->
                <!-- hgcs_33 -->
                <!-- hgcs_34 -->
                <!-- hgcs_35 -->
                <!-- hgcs_36 -->
                <!-- hgcs_37 -->
                <!-- hgcs_38 -->
                <!-- hgcs_39 -->
                <!-- hgcs_40 -->
                <!-- hgcs_41 -->
                <!-- hgcs_42 -->
                <!-- hgcs_43 -->
                <!-- hgcs_44 -->
                <!-- hgcs_45 -->
                <!-- hgcs_46 -->
                <!-- hgcs_47 -->
                <!-- hgcs_48 -->
                <!-- hgcs_49 -->
                <!-- hgcs_50 -->
                <!-- hgcs_51 -->
                <!-- hgcs_52 -->
                <!-- hgcs_53 -->
                <!-- hgcs_54 -->
                <!-- hgcs_55 -->
                <!-- hgcs_56 -->
                <!-- hgcs_57 -->
                <!-- hgcs_58 -->
                <!-- hgcs_59 -->
                <!-- hgcs_60 -->
                <!-- hgcs_61 -->
                <!-- hgcs_62 -->
                <!-- hgcs_63 -->
                <!-- hgcs_64 -->
                <!-- hgcs_65 -->
                <!-- hgcs_66 -->
                <!-- hgcs_67 -->
                <!-- hgcs_68 -->
                <!-- hgcs_69 -->
                <!-- hgcs_70 -->
                <!-- hgcs_71 -->
                <!-- hgcs_72 -->
                <!-- hgcs_73 -->
                <!-- hgcs_74 -->
                <!-- hgcs_75 -->
                <!-- hgcs_76 -->
                <!-- hgcs_77 -->
                <!-- hgcs_78 -->
                <!-- hgcs_79 -->
                <!-- hgcs_80 -->
                <!-- hgcs_81 -->
                <!-- hgcs_82 -->
                <!-- hgcs_83 -->
                <!-- hgcs_84 -->
                <!-- hgcs_85 -->
                <!-- hgcs_86 -->
                <!-- hgcs_87 -->
                <!-- hgcs_88 -->
                <!-- hgcs_89 -->
                <!-- hgcs_90 -->
                <!-- hgcs_91 -->
                <!-- hgcs_92 -->
                <!-- hgcs_93 -->
                <!-- hgcs_94 -->
                <!-- hgcs_95 -->
                <!-- hgcs_96 -->
                <!-- hgcs_97 -->
                <!-- hgcs_98 -->
                <!-- hgcs_99 -->
                <!-- hgcs_100 -->
            </ul>
        </main>
        <script>
            // JavaScript to toggle email details visibility
            const emailItems = document.querySelectorAll('.email-item');
            
            emailItems.forEach(emailItem => {
                emailItem.addEventListener('click', () => {
                    emailItem.classList.toggle('expanded');
                });
            });
        
            // JavaScript to reload the inbox
            const reloadButton = document.getElementById('reloadInbox');
            reloadButton.addEventListener('click', () => {
                reloadButton.classList.add('animate');
                setTimeout(function() {
                    reloadButton.classList.remove('animate');
                }, 1000);
                location.reload();
            });
        
            // JavaScript to reload the inbox every 10 seconds
            const reloadEvery7Seconds = () => {
                location.reload();
            };
        
            // Call the reload function initially and then every 10 seconds
            setTimeout(reloadEvery7Seconds, 7000); // Call it initially
        </script>
        
    </body>
    </html>
    '''
    with open(f"templates/{inboxfile}", "w") as file:
            file.write(Inner_html)




try:
    arguments  = sys.argv
    password   = arguments[1]
    port       = arguments[2]
    jsonfile   = arguments[3]
    loginfile  = arguments[4]
    inboxfile  = arguments[5]
    host       = arguments[6]
    localhost(password, port, jsonfile, loginfile, inboxfile, host)
    exit()
except IndexError: pass

