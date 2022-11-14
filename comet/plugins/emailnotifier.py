from comet.plugins.utils import Utils
from comet.plugins.mail import Mail
import json

class EmailNotifier(object):

    def __init__(self):
        
        f = open('/usr/local/comet_voevent_reciver_config/config.json')
        config = json.load(f)
        self.mail = Mail(config["sender_email"], config["sender_email_password"])
        self.to = config["email_recivers"]
        self.packet_with_email_notification = config["packet_with_email_notification"]

    def sendEmails(self, voeventdata, result_row):
        
        
        if voeventdata.packet_type in self.packet_with_email_notification or voeventdata.is_ste: #it will send an email for GW, Neutrino event or STE events

            subject = f'Notice alert for {voeventdata.name}'

            body = f'The AFIS platform received a notice for the {voeventdata.name} event at {voeventdata.UTC} for triggerID {voeventdata.trigger_id} {chr(10)} available at \
            http://afiss.iasfbo.inaf.it/afiss/full_results.html?instrument_name={voeventdata.name}&trigger_time_utc={voeventdata.UTC}&trigger_id={Utils.graceID_from_triggerId(voeventdata.name, voeventdata.trigger_id)}&seqnum={voeventdata.seqNum}'

            self.mail.send_email(self.to, subject, body)
        
        #check if there are correlated instruments and send an email if so

        if result_row:
            subject = f'Correlations for {voeventdata.name}'

            body = f'The AFIS platform received a notice for the {voeventdata.name} at {voeventdata.UTC} for triggerID {voeventdata.trigger_id} {chr(10)} available at \
            http://afiss.iasfbo.inaf.it/afiss/full_results.html?instrument_name={voeventdata.name}&trigger_time_utc={voeventdata.UTC}&trigger_id={Utils.graceID_from_triggerId(voeventdata.name, voeventdata.trigger_id)}&seqnum={voeventdata.seqNum} {chr(10)} with the following correlated events: {chr(10)} {str(result_row)}'

            self.mail.send_email(self.to, subject, body)