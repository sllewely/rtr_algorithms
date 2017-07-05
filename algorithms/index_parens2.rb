
def find_all_parens(sample_string)
  all_parens = []
  open_parens = []
  sample_string.chars.each_with_index do |c, i|
    if c == '('
      open_parens.push(i)
    elsif c == ')'
      if open_parens.empty?
        return false
      end
      all_parens << [open_parens.pop, i]
    end
  end
  return false unless open_parens.empty?
  all_parens
end

open_parens = [0, 3]
closed_parens = [[1, 2], [3, 4], [0, 5]]
