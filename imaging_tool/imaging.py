import subprocess


def image_disk(source_disk, dest_path, progress_callback):
    dd_command = ['dd', f'if={source_disk}', f'of={dest_path}', 'bs=4M', 'status=progress']

    process = subprocess.Popen(dd_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    total_size = get_disk_size(source_disk)
    copied_size = 0

    while True:
        output = process.stderr.readline()
        if not output and process.poll() is not None:
            break
        if output:
            print(output.strip())
            if 'bytes' in output:
                copied_size = extract_copied_size(output)
                progress = (copied_size / total_size) * 100
                progress_callback.emit(progress)

    if process.returncode != 0:
        raise Exception("dd command failed")


def get_disk_size(source_disk):
    lsblk_command = ['lsblk', '-bno', 'SIZE', source_disk]
    process = subprocess.run(lsblk_command, capture_output=True, text=True, check=True)
    return int(process.stdout.strip())


def extract_copied_size(output):
    # Extract the copied size from the dd output
    try:
        return int(output.split()[0])
    except ValueError:
        return 0
