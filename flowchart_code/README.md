# Flowchart Source Files

Graphviz `.dot` files for project report flowcharts.

## Compile to PDF

```bash
# Original pipeline
dot -Tpdf concussion_detection_pipeline.dot -o ../figures/concussion_detection_pipeline.pdf

# Pipeline with our solution
dot -Tpdf concussion_detection_with_solution.dot -o ../figures/concussion_detection_with_solution.pdf
```

## Install Graphviz

```bash
sudo apt-get install graphviz  # Ubuntu/Debian
brew install graphviz          # macOS
```
