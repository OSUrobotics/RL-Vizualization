# RL-Vizualization

## Overview
This repository provides a graphical user interface (GUI) for generating figures from Reinforcement Learning (RL) evaluation data. It aims to simplify the visualization process by offering a modular approach using abstract base classes. Users can develop their own plotting scripts using these base classes to suit their specific needs.

## Features
- GUI for interactive data visualization.
- Abstract base classes for defining custom plotting scripts.
- Supports various RL evaluation metrics and data formats.
- Export figures in multiple formats (e.g., PNG, SVG).

## Installation

### Requirements
- Python 3.x
- Dependencies listed in `requirements.txt`

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/rl-evaluation-plotting.git
   cd rl-evaluation-plotting
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Plotting is implemented for a selection of environments linked in `compatible environments.txt`

Plotting for your specific environment will need to be developed (see Devloping Custom Plotting Scripts)


### Running the GUI
To start the GUI for plotting evaluation data from the mojograsp environment:

```bash
python Data_analysis_gui.py
```

### Developing Custom Plotting Scripts
1. **Extend Base Classes**: Implement your custom plotting logic by extending the provided abstract base classes (`BasePlotter` and `DataLoader`). This allows you to integrate your specific RL evaluation data and plotting requirements seamlessly into the GUI.

2. **Example Script**:
   ```python
   from backend_base import BasePlotter
   from data_loading_base import DataLoader

   class CustomPlotter(BasePlotter):
       def draw_my_plot(self, data):
           # Custom plotting logic using matplotlib or other libraries
           pass

   class CustomDataLoader(DataLoader):
       def load_data(self, file_path):
           # Custom data loading logic for your RL evaluation data format
           return RL_dataframe
   ```

3. **Integrating Custom Scripts**: Integrate your custom plotting scripts into the GUI by modifying the `gui.py` file or using as standalone scripts.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or support, please contact [your_email@example.com](mailto:your_email@example.com).

---

Feel free to customize this template further based on specific features, dependencies, or guidelines relevant to your project. Adjust the sections and details as necessary to best reflect the functionality and purpose of your repository.