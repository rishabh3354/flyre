from engine import SIZE, App, IntegerScaleScreen
from states.loading import LoadingState

if __name__ == "__main__":
    App(LoadingState, IntegerScaleScreen(SIZE)).run()
