import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt


# function f(x) = sin(x)
def f(x):
    return np.sin(x)


# monte carlo
def monte_carlo(a, b):
    N = 1000  # count of random points
    x_random = np.random.uniform(a, b, N)
    y_random = np.random.uniform(0, 1, N)  # sin(x) ≤ 1 for all "x" on intergal [0, π]
    # gray part sin(x)
    under_curve = y_random < f(x_random)
    integral_mc = (b - a) * 1 * np.mean(under_curve)
    # quad
    result_quad, error_quad = spi.quad(f, a, b)
    # show result
    print('---------------------------------------------------------')
    print(f"Integral by Monte-Carlo: {integral_mc}")
    print('---------------------------------------------------------')
    print(f"Integral by quad: {result_quad}, error: {error_quad}")
    print('---------------------------------------------------------')


# Main
if __name__ == '__main__':
    try:
        # limits of integration
        a = 0 
        b = np.pi
        # monte carlo
        monte_carlo(a, b)
        #visualisation
        x = np.linspace(0, np.pi, 400)
        y = f(x)
        fig, ax = plt.subplots()
        ax.plot(x, y, 'r', linewidth=2)
        ix = np.linspace(a, b)
        iy = f(ix)
        ax.fill_between(ix, iy, color='gray', alpha=0.3)
        ax.set_xlim([0, np.pi])
        ax.set_ylim([0, 1.1])
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.axvline(x=a, color='gray', linestyle='--')
        ax.axvline(x=b, color='gray', linestyle='--')
        ax.set_title('Integral f(x) = sin(x) from 0 to π')
        plt.grid(True)
        plt.show()
    except (ValueError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)

