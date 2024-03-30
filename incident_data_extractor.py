from bs4 import BeautifulSoup
import os
import csv

class IncidentDataExtractor:
    def __init__(self, wiki_folder_path):
        self.wiki_folder_path = wiki_folder_path

    def find_detail_info(self, soup, label_text):
        """Safely find detail info based on the label text."""
        # Find the label span by its text content
        label = soup.find("span", class_="detail-label", string=lambda text: label_text in text)
        if label:
            # Attempt to find the next sibling that is a span with class 'detail-info'
            detail_info = label.find_next_sibling("span", class_="detail-info")
            if detail_info:
                return detail_info.text.strip()
        return "Not Available"  # Default text or handle as appropriate

    def extract_incident_data(self, html_content):
        """Extracts incident data from a single HTML content using CSS selectors."""
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extracting data using CSS class names and handling missing elements
        data = {
            'Incident ID': self.find_detail_info(soup, "Incident ID:"),
            'Title': self.find_detail_info(soup, "Title:"),
            'Date and Time': self.find_detail_info(soup, "Date and Time:"),
            'Reported By': self.find_detail_info(soup, "Reported By:"),
            'Component Affected': self.find_detail_info(soup, "Component Affected:"),
            'Resolution Steps': " ".join(p.text.strip() for p in soup.select(".resolution-steps > p:not(:has(span))")),
            'Resolved By': self.find_detail_info(soup, "Resolved By:"),
            'Resolution Date and Time': self.find_detail_info(soup, "Resolution Date and Time:"),
            'Current Status': soup.select_one(".incident-status p").text.strip() if soup.select_one(
                ".incident-status p") else "Not Available",
            'Lessons Learned': soup.select_one(".lessons-learned p").text.strip() if soup.select_one(
                ".lessons-learned p") else "Not Available",
        }
        return data

    def load_incidents(self):
        incidents_data = []

        # Get list of HTML files in the directory
        files = os.listdir(self.wiki_folder_path)

        # Iterate through each HTML file
        for filename in files:
            file_path = os.path.join(self.wiki_folder_path, filename)
            file = open(file_path, 'r', encoding='utf-8')
            try:
                # Read the HTML content
                html_content = file.read()
                # Extract incident data from HTML
                incident_data = self.extract_incident_data(html_content)
                incidents_data.append(incident_data)
            except FileNotFoundError:
                print("File not found:", file_path)
            except Exception as e:
                print("An error occurred while opening the file:", e)
            finally:
                file.close()

        return incidents_data

    def convert_to_csv(self, incidents_data, csv_file_name):
        try:
            # Open a new CSV file in write mode
            with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
                # Create a CSV DictWriter object with the field names
                writer = csv.DictWriter(file, fieldnames=incidents_data[0].keys())

                # Write the header (column names)
                writer.writeheader()

                # Write the data rows
                for incident in incidents_data:
                    writer.writerow(incident)

            print(f'Data has been written to {csv_file_name}')
            return True
        except FileNotFoundError:
            print("File not found:", csv_file_name)
            return False
        except Exception as e:
            print("An error occurred while opening the file:", e)
            return False
