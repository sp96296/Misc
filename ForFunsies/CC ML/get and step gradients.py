def get_gradient_at_b(x, y, m, b):
  values = [(yVal-(m*xVal+b)) for yVal, xVal in zip(y, x)]
  diff = sum(values)
  shorter = x if len(x) < len(y) else y
  N = len(shorter)
  b_gradient = diff*(-2/N)
  return b_gradient

def get_gradient_at_m(x,y,m,b):
  values = [(xVal*(yVal-(m*xVal+b))) for yVal, xVal in zip(y, x)]
  diff = sum(values)
  shorter = x if len(x) < len(y) else y
  N = len(shorter)
  m_gradient = diff*(-2/N)
  return m_gradient

# Define your step_gradient function here
def step_gradient(x, y, b_current, m_current):
  b_gradient = get_gradient_at_b(x, y, b_current, m_current)
  m_gradient = get_gradient_at_m(x, y, b_current, m_current)
  b = b_current - (0.01 * b_gradient)
  m = m_current - (0.01 * m_gradient)
  gradients = [b_gradient, m_gradient]
  return b, m