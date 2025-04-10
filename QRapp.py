import tkinter as tk
from tkinter import messagebox, filedialog
import cv2
from pyzbar.pyzbar import decode
import qrcode
from PIL import Image, ImageTk
import threading

class QRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Scanner & Generator")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # Title
        tk.Label(root, text="📷 QR Code App", font=("Helvetica", 20, "bold")).pack(pady=10)

        # --- QR Code Generator ---
        gen_frame = tk.LabelFrame(root, text="Generate QR Code", padx=10, pady=10)
        gen_frame.pack(padx=10, pady=10, fill="both")

        self.qr_input = tk.Entry(gen_frame, font=("Helvetica", 14))
        self.qr_input.pack(fill="x", padx=5, pady=5)

        tk.Button(gen_frame, text="Generate", command=self.generate_qr).pack(pady=5)
        self.qr_label = tk.Label(gen_frame)
        self.qr_label.pack(pady=5)

        tk.Button(gen_frame, text="Save QR Code", command=self.save_qr).pack(pady=5)

        # --- QR Code Scanner ---
        scan_frame = tk.LabelFrame(root, text="Scan QR Code", padx=10, pady=10)
        scan_frame.pack(padx=10, pady=10, fill="both")

        tk.Button(scan_frame, text="Start Scanning", command=self.start_scanner).pack(pady=5)
        self.scan_result = tk.Label(scan_frame, text="Result: ", font=("Helvetica", 12), wraplength=400)
        self.scan_result.pack(pady=5)

        self.cap = None
        self.qr_image = None

    def generate_qr(self):
        data = self.qr_input.get()
        if data:
            qr = qrcode.make(data)
            self.qr_image = qr
            qr = qr.resize((200, 200))
            img = ImageTk.PhotoImage(qr)
            self.qr_label.configure(image=img)
            self.qr_label.image = img
        else:
            messagebox.showwarning("Input Error", "Please enter data to generate QR code.")

    def save_qr(self):
        if self.qr_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png")])
            if file_path:
                self.qr_image.save(file_path)
                messagebox.showinfo("Saved", "QR code saved successfully.")
        else:
            messagebox.showwarning("No QR", "Generate a QR code first.")

    def start_scanner(self):
        threading.Thread(target=self.scan_qr, daemon=True).start()

    def scan_qr(self):
        self.cap = cv2.VideoCapture(0)
        found_data = None

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            for barcode in decode(frame):
                data = barcode.data.decode('utf-8')
                found_data = data
                pts = barcode.polygon
                pts = [(pt.x, pt.y) for pt in pts]
                cv2.polylines(frame, [np.array(pts, dtype=np.int32)], True, (0, 255, 0), 2)
                cv2.putText(frame, data, (pts[0][0], pts[0][1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            cv2.imshow("QR Scanner - Press Q to close", frame)

            if cv2.waitKey(1) & 0xFF == ord('q') or found_data:
                break

        self.cap.release()
        cv2.destroyAllWindows()

        if found_data:
            self.scan_result.config(text="Result: " + found_data)
        else:
            self.scan_result.config(text="Result: No QR code found")

# ---- Run the app ----
if __name__ == "__main__":
    import numpy as np
    root = tk.Tk()
    app = QRApp(root)
    root.mainloop()
